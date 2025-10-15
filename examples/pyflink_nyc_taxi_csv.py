#!/usr/bin/env python3
"""
PyFlink Big Data Pipeline - NYC Taxi Dataset (CSV Version)
===========================================================

Versão simplificada usando CSV ao invés de Parquet para evitar conflitos de dependências.

Dataset: NYC Yellow Taxi Trip Records
Formato: CSV (mais simples, menos dependências)
Tamanho: ~3M registros, ~500MB CSV

Análises:
1. Top 10 rotas mais populares
2. Receita por hora do dia
3. Viagens por dia da semana
"""

from pyflink.table import EnvironmentSettings, TableEnvironment
import argparse
import os
import sys


def download_and_convert_dataset(parquet_path: str, csv_path: str):
    """Baixa dataset Parquet e converte para CSV se necessário."""
    
    if os.path.exists(csv_path):
        print(f"✓ Dataset CSV já existe: {csv_path}")
        return
    
    if not os.path.exists(parquet_path):
        print("📥 Baixando NYC Taxi dataset...")
        import urllib.request
        url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
        os.makedirs(os.path.dirname(parquet_path), exist_ok=True)
        
        try:
            urllib.request.urlretrieve(url, parquet_path)
            print(f"✓ Download concluído: {parquet_path}")
        except Exception as e:
            print(f"❌ Erro ao baixar: {e}")
            sys.exit(1)
    
    # Converter para CSV
    print("🔄 Convertendo Parquet para CSV...")
    try:
        import pandas as pd
        df = pd.read_parquet(parquet_path)
        
        # Selecionar apenas colunas necessárias para reduzir tamanho
        columns_needed = [
            'tpep_pickup_datetime', 'tpep_dropoff_datetime',
            'passenger_count', 'trip_distance', 
            'PULocationID', 'DOLocationID',
            'payment_type', 'fare_amount', 'tip_amount', 'total_amount'
        ]
        df = df[columns_needed]
        
        # Converter para CSV
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df.to_csv(csv_path, index=False)
        
        print(f"✓ CSV criado: {csv_path}")
        print(f"  Registros: {len(df):,}")
        print(f"  Tamanho: {os.path.getsize(csv_path) / 1024**2:.1f} MB")
        
    except ImportError:
        print("❌ Pandas não instalado. Execute:")
        print("   pip install pandas pyarrow")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro na conversão: {e}")
        sys.exit(1)


def create_taxi_table(t_env: TableEnvironment, csv_path: str):
    """Cria tabela Flink a partir do CSV."""
    
    abs_path = os.path.abspath(csv_path)
    
    t_env.execute_sql(f"""
        CREATE TABLE taxi_trips (
            tpep_pickup_datetime STRING,
            tpep_dropoff_datetime STRING,
            passenger_count DOUBLE,
            trip_distance DOUBLE,
            PULocationID BIGINT,
            DOLocationID BIGINT,
            payment_type BIGINT,
            fare_amount DOUBLE,
            tip_amount DOUBLE,
            total_amount DOUBLE
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file://{abs_path}',
            'format' = 'csv',
            'csv.ignore-parse-errors' = 'true',
            'csv.allow-comments' = 'true'
        )
    """)
    
    print("✓ Tabela 'taxi_trips' criada")


def analysis_1_top_routes(t_env: TableEnvironment, output_dir: str):
    """Análise 1: Top 10 rotas mais populares."""
    
    print("\n📊 Análise 1: Top 10 Rotas Mais Populares")
    print("=" * 60)
    
    # Criar sink
    output_path = os.path.abspath(f"{output_dir}/top_routes")
    t_env.execute_sql(f"""
        CREATE TABLE top_routes_sink (
            pickup_location BIGINT,
            dropoff_location BIGINT,
            trip_count BIGINT
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file://{output_path}',
            'format' = 'csv'
        )
    """)
    
    # Query
    result = t_env.sql_query("""
        SELECT 
            PULocationID as pickup_location,
            DOLocationID as dropoff_location,
            COUNT(*) as trip_count
        FROM taxi_trips
        WHERE PULocationID IS NOT NULL 
          AND DOLocationID IS NOT NULL
        GROUP BY PULocationID, DOLocationID
        ORDER BY trip_count DESC
        LIMIT 10
    """)
    
    # Executar
    result.execute_insert('top_routes_sink').wait()
    print(f"✓ Resultados salvos em: {output_path}/")


def analysis_2_revenue_by_hour(t_env: TableEnvironment, output_dir: str):
    """Análise 2: Receita por hora do dia."""
    
    print("\n📊 Análise 2: Receita por Hora do Dia")
    print("=" * 60)
    
    output_path = os.path.abspath(f"{output_dir}/revenue_by_hour")
    t_env.execute_sql(f"""
        CREATE TABLE revenue_by_hour_sink (
            hour_of_day INT,
            total_trips BIGINT,
            total_revenue DOUBLE,
            avg_fare DOUBLE
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file://{output_path}',
            'format' = 'csv'
        )
    """)
    
    # Query - extrair hora da string datetime
    result = t_env.sql_query("""
        SELECT 
            CAST(SUBSTRING(tpep_pickup_datetime, 12, 2) AS INT) as hour_of_day,
            COUNT(*) as total_trips,
            SUM(total_amount) as total_revenue,
            AVG(fare_amount) as avg_fare
        FROM taxi_trips
        WHERE tpep_pickup_datetime IS NOT NULL
          AND total_amount > 0
        GROUP BY CAST(SUBSTRING(tpep_pickup_datetime, 12, 2) AS INT)
        ORDER BY hour_of_day
    """)
    
    result.execute_insert('revenue_by_hour_sink').wait()
    print(f"✓ Resultados salvos em: {output_path}/")


def analysis_3_trips_by_distance(t_env: TableEnvironment, output_dir: str):
    """Análise 3: Distribuição de viagens por distância."""
    
    print("\n📊 Análise 3: Viagens por Faixa de Distância")
    print("=" * 60)
    
    output_path = os.path.abspath(f"{output_dir}/trips_by_distance")
    t_env.execute_sql(f"""
        CREATE TABLE trips_by_distance_sink (
            distance_range STRING,
            trip_count BIGINT,
            avg_fare DOUBLE,
            avg_duration_min DOUBLE
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file://{output_path}',
            'format' = 'csv'
        )
    """)
    
    result = t_env.sql_query("""
        SELECT 
            CASE 
                WHEN trip_distance < 1 THEN '0-1 miles'
                WHEN trip_distance < 3 THEN '1-3 miles'
                WHEN trip_distance < 5 THEN '3-5 miles'
                WHEN trip_distance < 10 THEN '5-10 miles'
                ELSE '10+ miles'
            END as distance_range,
            COUNT(*) as trip_count,
            AVG(fare_amount) as avg_fare,
            AVG(trip_distance / 30.0 * 60) as avg_duration_min
        FROM taxi_trips
        WHERE trip_distance > 0 
          AND trip_distance < 100
          AND fare_amount > 0
        GROUP BY 
            CASE 
                WHEN trip_distance < 1 THEN '0-1 miles'
                WHEN trip_distance < 3 THEN '1-3 miles'
                WHEN trip_distance < 5 THEN '3-5 miles'
                WHEN trip_distance < 10 THEN '5-10 miles'
                ELSE '10+ miles'
            END
    """)
    
    result.execute_insert('trips_by_distance_sink').wait()
    print(f"✓ Resultados salvos em: {output_path}/")


def main():
    parser = argparse.ArgumentParser(description='PyFlink NYC Taxi Pipeline (CSV)')
    parser.add_argument('--download', action='store_true', 
                       help='Baixar e converter dataset para CSV')
    parser.add_argument('--data', default='data/real/nyc_taxi_2023_01.csv',
                       help='Caminho para CSV do dataset')
    parser.add_argument('--output', default='data/output/nyc_taxi_analysis',
                       help='Diretório de saída')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🚕 PyFlink Big Data Pipeline - NYC Taxi (CSV)")
    print("=" * 60)
    
    # Download/conversão se necessário
    if args.download or not os.path.exists(args.data):
        parquet_path = 'data/real/nyc_taxi_2023_01.parquet'
        download_and_convert_dataset(parquet_path, args.data)
    else:
        print(f"✓ Usando dataset existente: {args.data}")
    
    # Configurar PyFlink
    print("\n⚙️  Configurando ambiente PyFlink...")
    env_settings = EnvironmentSettings.in_batch_mode()
    t_env = TableEnvironment.create(env_settings)
    t_env.get_config().set("parallelism.default", "2")
    
    # Criar tabela
    create_taxi_table(t_env, args.data)
    
    # Executar análises
    print("\n🔄 Executando análises...")
    
    try:
        analysis_1_top_routes(t_env, args.output)
        analysis_2_revenue_by_hour(t_env, args.output)
        analysis_3_trips_by_distance(t_env, args.output)
        
        print("\n" + "=" * 60)
        print("✅ Pipeline concluído com sucesso!")
        print("=" * 60)
        print(f"\n📁 Resultados em: {os.path.abspath(args.output)}/")
        
        # Listar arquivos gerados
        for root, dirs, files in os.walk(args.output):
            for file in files:
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath)
                print(f"  - {filepath} ({size:,} bytes)")
                
    except Exception as e:
        print(f"\n❌ Erro durante execução: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
