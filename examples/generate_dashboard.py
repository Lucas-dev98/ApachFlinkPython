#!/usr/bin/env python3
"""
Gerador de Dashboard HTML para visualização dos resultados das análises
"""

import os
import json
import csv
from datetime import datetime
from typing import Dict, List, Any


def read_csv_results(file_path: str) -> List[Dict[str, str]]:
    """Lê arquivo CSV e retorna lista de dicionários"""
    results = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            results = list(reader)
    return results


def load_execution_report(report_path: str) -> Dict[str, Any]:
    """Carrega relatório de execução JSON"""
    if os.path.exists(report_path):
        with open(report_path, 'r') as f:
            return json.load(f)
    return {}


def generate_html_dashboard(output_dir: str, html_output: str = "data/output/dashboard.html"):
    """Gera dashboard HTML com resultados das análises"""
    
    # Localizar arquivos CSV (part-*)
    import glob
    
    top_routes_files = glob.glob(f"{output_dir}/top_routes/part-*")
    revenue_files = glob.glob(f"{output_dir}/revenue_by_hour/part-*")
    distance_files = glob.glob(f"{output_dir}/trips_by_distance/part-*")
    
    # Carregar dados
    top_routes = read_csv_results(top_routes_files[0]) if top_routes_files else []
    revenue = read_csv_results(revenue_files[0]) if revenue_files else []
    distance = read_csv_results(distance_files[0]) if distance_files else []
    
    # Carregar relatório de execução
    report = load_execution_report(f"{output_dir}/execution_report.json")
    
    # Gerar HTML
    html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYC Taxi Analysis - Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        
        h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .subtitle {{
            color: #666;
            font-size: 1.1em;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }}
        
        .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
        }}
        
        .stat-label {{
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .analysis-section {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        
        .analysis-section h2 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.8em;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        
        th {{
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        tr:hover {{
            background: #f5f5f5;
        }}
        
        .chart-bar {{
            height: 30px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 5px;
            transition: all 0.3s;
        }}
        
        .chart-bar:hover {{
            transform: scaleX(1.05);
        }}
        
        .timestamp {{
            text-align: center;
            color: white;
            margin-top: 20px;
            font-size: 0.9em;
        }}
        
        .icon {{
            font-size: 2em;
            margin-bottom: 10px;
        }}
        
        .success {{
            color: #4caf50;
        }}
        
        .warning {{
            color: #ff9800;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚕 NYC Taxi Analysis Dashboard</h1>
            <p class="subtitle">Análise de dados do NYC Yellow Taxi - Janeiro 2023</p>
        </header>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="icon">📊</div>
                <div class="stat-label">Registros Processados</div>
                <div class="stat-value">{report.get('statistics', {}).get('records_processed', 0):,}</div>
            </div>
            <div class="stat-card">
                <div class="icon">✅</div>
                <div class="stat-label">Análises Concluídas</div>
                <div class="stat-value">{report.get('statistics', {}).get('analyses_completed', 0)}</div>
            </div>
            <div class="stat-card">
                <div class="icon">⏱️</div>
                <div class="stat-label">Tempo de Execução</div>
                <div class="stat-value">{report.get('execution_time_seconds', 0):.1f}s</div>
            </div>
            <div class="stat-card">
                <div class="icon">{'✓' if report.get('success') else '⚠'}</div>
                <div class="stat-label">Status</div>
                <div class="stat-value {'success' if report.get('success') else 'warning'}">
                    {'Sucesso' if report.get('success') else 'Avisos'}
                </div>
            </div>
        </div>
        
        <!-- Análise 1: Top Rotas -->
        <div class="analysis-section">
            <h2>📍 Top 10 Rotas Mais Populares</h2>
            <p>As rotas com maior volume de viagens entre pontos de embarque e desembarque.</p>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Local Embarque</th>
                        <th>Local Desembarque</th>
                        <th>Viagens</th>
                        <th>Visualização</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # Adicionar dados de top rotas
    routes_data = [row for row in top_routes if row.get('trip_count', '').isdigit()]
    max_trips = max([int(row.get('trip_count', 0)) for row in routes_data], default=1) if routes_data else 1
    for idx, row in enumerate(routes_data[:10], 1):
        trip_count = int(row.get('trip_count', 0))
        bar_width = (trip_count / max_trips) * 100
        html += f"""
                    <tr>
                        <td><strong>{idx}</strong></td>
                        <td>Zona {row.get('pickup_location', 'N/A')}</td>
                        <td>Zona {row.get('dropoff_location', 'N/A')}</td>
                        <td><strong>{trip_count:,}</strong></td>
                        <td><div class="chart-bar" style="width: {bar_width}%"></div></td>
                    </tr>
        """
    
    html += """
                </tbody>
            </table>
        </div>
        
        <!-- Análise 2: Receita por Hora -->
        <div class="analysis-section">
            <h2>💰 Receita por Hora do Dia</h2>
            <p>Distribuição de receita e viagens ao longo das 24 horas.</p>
            <table>
                <thead>
                    <tr>
                        <th>Hora</th>
                        <th>Total Viagens</th>
                        <th>Receita Total</th>
                        <th>Tarifa Média</th>
                        <th>Volume</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # Adicionar dados de receita
    revenue_data = [row for row in revenue if row.get('hour_of_day', '').isdigit()]
    max_revenue = max([float(row.get('total_revenue', 0)) for row in revenue_data], default=1) if revenue_data else 1
    for row in revenue_data:
        total_revenue = float(row.get('total_revenue', 0))
        bar_width = (total_revenue / max_revenue) * 100
        html += f"""
                    <tr>
                        <td><strong>{row.get('hour_of_day', 'N/A')}:00</strong></td>
                        <td>{int(float(row.get('total_trips', 0))):,}</td>
                        <td>${total_revenue:,.2f}</td>
                        <td>${float(row.get('avg_fare', 0)):.2f}</td>
                        <td><div class="chart-bar" style="width: {bar_width}%"></div></td>
                    </tr>
        """
    
    html += """
                </tbody>
            </table>
        </div>
        
        <!-- Análise 3: Viagens por Distância -->
        <div class="analysis-section">
            <h2>📏 Distribuição por Distância</h2>
            <p>Análise de viagens agrupadas por faixas de distância.</p>
            <table>
                <thead>
                    <tr>
                        <th>Faixa de Distância</th>
                        <th>Viagens</th>
                        <th>Tarifa Média</th>
                        <th>Duração Média (min)</th>
                        <th>Proporção</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # Adicionar dados de distância
    distance_data = [row for row in distance if row.get('trip_count', '') and row.get('trip_count', '').replace('.', '').isdigit()]
    total_distance_trips = sum([int(float(row.get('trip_count', 0))) for row in distance_data])
    for row in distance_data:
        trip_count = int(float(row.get('trip_count', 0)))
        percentage = (trip_count / total_distance_trips * 100) if total_distance_trips > 0 else 0
        html += f"""
                    <tr>
                        <td><strong>{row.get('distance_range', 'N/A')}</strong></td>
                        <td>{trip_count:,}</td>
                        <td>${float(row.get('avg_fare', 0)):.2f}</td>
                        <td>{float(row.get('avg_duration_min', 0)):.1f} min</td>
                        <td><div class="chart-bar" style="width: {percentage}%"></div></td>
                    </tr>
        """
    
    timestamp = report.get('timestamp', datetime.now().isoformat())
    html += f"""
                </tbody>
            </table>
        </div>
        
        <div class="timestamp">
            <p>Dashboard gerado em: {datetime.fromisoformat(timestamp).strftime('%d/%m/%Y %H:%M:%S')}</p>
            <p>Powered by Apache Flink + PyFlink</p>
        </div>
    </div>
</body>
</html>
    """
    
    # Salvar HTML
    os.makedirs(os.path.dirname(html_output), exist_ok=True)
    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Dashboard HTML gerado: {os.path.abspath(html_output)}")
    return os.path.abspath(html_output)


if __name__ == "__main__":
    import sys
    
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "data/output/nyc_taxi_analysis"
    html_path = generate_html_dashboard(output_dir)
    
    print(f"\n🌐 Abra no navegador: file://{html_path}")
