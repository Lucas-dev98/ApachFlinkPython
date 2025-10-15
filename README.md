# Apache Flink + PyFlink - Big Data Pipeline# apacheFlink — ambiente local de desenvolvimento



Projeto completo de processamento de Big Data usando **Apache Flink** e **PyFlink** com dataset real (NYC Taxi Trip Records).Este diretório contém scripts para configurar um ambiente local de desenvolvimento com Apache Flink (binário).



## 📋 RequisitosArquivos principais:



- **Java 11+** (JDK instalado)- `setup.sh` — baixa e extrai a distribuição binária do Flink (padrão: 1.18.1). Use `--set-env` para adicionar variáveis ao `~/.bashrc`.

- **Python 3.10** (via pyenv)- `start-flink.sh` — inicia um cluster Flink local (jobmanager + taskmanager).

- **Linux/macOS** (testado em Ubuntu)- `stop-flink.sh` — para o cluster local.



## 🚀 Início RápidoEnvironment file

----------------

### 1. Configurar Ambiente

After running `./setup.sh` the script will generate `env.sh` in the project root. This file contains:

```bash

# Executar setup (baixa Flink e cria env.sh)- `FLINK_HOME` and `PATH` entries pointing to the extracted Flink binary

./setup.sh- If a Python virtualenv exists at `./venv`, `env.sh` will add the virtualenv `bin` to `PATH` and set `VIRTUAL_ENV`.



# Carregar variáveis de ambienteYou can load it manually with:

source env.sh

```bash

# Ativar virtualenv Pythonsource ./env.sh

source venv_py310/bin/activate```

```

Or run `./setup.sh --set-env` to append a small `source ./env.sh` snippet to your `~/.bashrc`.

### 2. Iniciar Cluster Flink

Virtualenv (Python)

```bash--------------------

./start-flink.sh

```To create a Python virtual environment named `venv` and install PyFlink:



**Acesse a UI:** http://localhost:8081```bash

python3 -m venv venv

### 3. Executar Pipeline Big Datasource venv/bin/activate

pip install --upgrade pip

```bashpip install apache-flink==1.18.1

# Pipeline NYC Taxi (3 análises de Big Data)```

python examples/pyflink_nyc_taxi_csv.py --download

```The generated `env.sh` will automatically add `venv/bin` to `PATH` if `venv` exists.



### 4. Parar ClusterExemplos PyFlink

================

```bash

./stop-flink.sh## 1. Exemplo Simples: Top-N Customers

```

`examples/pyflink_topn.py` - demonstra um job batch básico usando Table API.

## 📁 Estrutura do ProjetoLê `data/sample_transactions.csv`, agrega por cliente e retorna top-N.



```## 2. Pipeline Big Data: NYC Taxi Dataset (COMPLETO)

apacheFlink/

├── env.sh                      # Variáveis de ambiente**🚕 `examples/pyflink_nyc_taxi.py`** - Pipeline completo com dados reais!

├── setup.sh                    # Instala Flink

├── start-flink.sh              # Inicia cluster### Dataset

├── stop-flink.sh               # Para cluster- **Fonte**: NYC Taxi and Limousine Commission (TLC)

├── run_pipeline.sh             # Automação completa- **Tamanho**: ~40MB (1 mês de dados - Janeiro 2023)

│- **Registros**: ~3 milhões de viagens

├── venv_py310/                 # Python 3.10 + PyFlink- **Formato**: Parquet (otimizado para análise)

│- **URL**: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

├── flink/                      # Apache Flink 1.18.1

│   └── apache-flink-1.18.1/### Análises Implementadas

│

├── examples/O pipeline executa 4 análises completas:

│   ├── pyflink_topn.py        # Exemplo Top-N

│   └── pyflink_nyc_taxi_csv.py # Pipeline Big Data1. **Top 10 Rotas Mais Populares**

│   - Agrega viagens por pickup/dropoff location IDs

└── data/                              - Identifica os pares de localizações mais frequentes

    ├── real/   - Output: `data/output/nyc_taxi_analysis/top_routes/`

    │   └── nyc_taxi_2023_01_filtered.csv

    └── output/2. **Receita por Hora do Dia**

        └── nyc_taxi_analysis/   - Agrega receita total por hora (0-23)

            ├── top_routes/   - Calcula média de tarifa por hora

            ├── revenue_by_hour/   - Útil para entender padrões de demanda

            └── trips_by_distance/   - Output: `data/output/nyc_taxi_analysis/revenue_by_hour/`

```

3. **Distância Média por Tipo de Pagamento**

## 🚕 Pipeline Big Data: NYC Taxi   - Agrupa por payment_type (1=Cartão, 2=Dinheiro, etc.)

   - Compara distância e valor médio por tipo

**Dataset:** NYC Yellow Taxi Trip Records (Janeiro 2023)   - Output: `data/output/nyc_taxi_analysis/distance_by_payment/`

- **Registros:** ~245,000 viagens

- **Tamanho:** ~50MB CSV4. **Análise de Gorjetas**

- **Fonte:** [NYC TLC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)   - Segmenta viagens por faixa de valor (0-10, 10-20, 20-30, 30-50, 50+)

   - Calcula gorjeta média e percentual por faixa

### Análises Implementadas   - Apenas pagamentos com cartão (dinheiro não registra gorjeta)

   - Output: `data/output/nyc_taxi_analysis/tip_analysis/`

#### 1️⃣ Top 10 Rotas Mais Populares

Identifica as 10 combinações pickup/dropoff location mais frequentes.### Como Funciona (Arquitetura)



#### 2️⃣ Receita por Hora do Dia```

Agrega receita total e média por hora (0-23h).[Dataset Parquet]

      ↓

#### 3️⃣ Distribuição por Distância[PyFlink Table API - Source]

Agrupa viagens por faixas: 0-1mi, 1-3mi, 3-5mi, 5-10mi, 10+mi.      ↓

[SQL Queries - Transformações]

### Executar  - GROUP BY

  - Agregações (COUNT, SUM, AVG)

```bash  - Window Functions (HOUR)

# Com download automático  - Filtros e CASE statements

python examples/pyflink_nyc_taxi_csv.py --download      ↓

[Filesystem Sink - CSV Output]

# Usando dataset existente      ↓

python examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv[Resultados em data/output/]

``````



### Resultados**Tecnologias utilizadas:**

- PyFlink Table API (abstração SQL sobre DataStream)

```- Parquet Reader (formato columnar eficiente)

data/output/nyc_taxi_analysis/- Batch Processing Mode (para dados históricos)

├── top_routes/part-*.csv- CSV Writer (resultados legíveis)

├── revenue_by_hour/part-*.csv

└── trips_by_distance/part-*.csv### Execução Automatizada

```

**Opção 1: Script Completo (Recomendado)**

## 📊 Exemplo Simples: Top-N

```bash

```bashchmod +x run_pipeline.sh

python examples/pyflink_topn.py \./run_pipeline.sh

    --input data/sample_transactions.csv \```

    --top 5

```O script `run_pipeline.sh` faz tudo automaticamente:

- ✓ Ativa ambiente Python (pyenv + venv)

## 🔧 Como Funciona- ✓ Verifica/instala Flink

- ✓ Inicia cluster local

### Arquitetura- ✓ Baixa dataset (~40MB download)

- ✓ Executa todas as 4 análises

```- ✓ Salva resultados

[CSV Dataset]- ✓ Mostra preview dos resultados

      ↓

[PyFlink Table API]**Opção 2: Passo a Passo Manual**

      ↓

[SQL Transformações]```bash

  - GROUP BY# 1. Ativar ambiente

  - Agregaçõessource venv_py310/bin/activate

  - ORDER BY + LIMITsource env.sh

      ↓

[CSV Output]# 2. Baixar Flink (se necessário)

```./setup.sh



### Tecnologias# 3. Iniciar cluster

./start-flink.sh

- **Apache Flink 1.18.1** - Motor distribuído

- **PyFlink** - Python API (Table API + SQL)# 4. Executar pipeline

- **CSV Connector** - Leitura/escrita filesystempython examples/pyflink_nyc_taxi.py --download



## 🛠️ Troubleshooting# 5. Ver resultados

ls -lh data/output/nyc_taxi_analysis/

### Java not found

```bash# 6. Parar cluster

java -version./stop-flink.sh

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64```

```

### Monitoramento

### ModuleNotFoundError: pyflink

```bashDurante a execução, você pode:

source venv_py310/bin/activate- **Acessar Flink WebUI**: http://localhost:8081

pip install apache-flink==1.18.1  - Ver jobs em execução

```  - Monitorar métricas (throughput, latência)

  - Verificar task managers

### Cluster não inicia  - Analisar logs

```bash

tail -f flink/apache-flink-1.18.1/log/*.log- **Ver logs em tempo real**:

./stop-flink.sh && ./start-flink.sh  ```bash

```  tail -f flink/apache-flink-1.18.1/log/flink-*-taskexecutor-*.out

  ```

## 📚 Documentação

### Resultados Esperados

- [Apache Flink](https://flink.apache.org/)

- [PyFlink Docs](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/)Após execução bem-sucedida, você terá:

- [Table API](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/)

```

## 🎯 Próximos Passosdata/output/nyc_taxi_analysis/

├── top_routes/

1. Adicionar análise de gorjetas│   └── *.csv              # Top 10 rotas

2. Implementar streaming em tempo real├── revenue_by_hour/

3. Deploy em cluster distribuído│   └── *.csv              # Receita por hora (24 linhas)

4. Integração com Kafka├── distance_by_payment/

│   └── *.csv              # Métricas por tipo pagamento

---└── tip_analysis/

    └── *.csv              # Análise gorjetas por faixa

**Desenvolvido com** ⚡ Apache Flink + 🐍 PyFlink```


**Exemplo de saída (top_routes):**
```
pickup_location,dropoff_location,trip_count
237,236,15234
236,237,14891
238,239,12456
...
```

### Conceitos de Big Data Demonstrados

1. **Batch Processing**: Processamento de dados históricos em lote
2. **Columnar Storage**: Uso de Parquet para eficiência
3. **SQL-based Analytics**: Queries SQL para análise de dados
4. **Distributed Computing**: Flink distribui trabalho entre workers
5. **Pipeline ETL**: Extract (Parquet) → Transform (SQL) → Load (CSV)

### Performance

Com o dataset de ~3M registros:
- **Tempo total**: ~30-60 segundos (depende do hardware)
- **Memória**: ~1-2GB RAM
- **Paralelismo**: Configurável (padrão: 2 slots)

Para datasets maiores, ajuste:
```python
t_env.get_config().set("parallelism.default", "4")  # Mais paralelismo
```

### Próximos Passos

Experimente modificar o pipeline:
- Adicionar mais análises SQL
- Processar múltiplos meses de dados
- Implementar janelas temporais (windowing)
- Adicionar mais sinks (PostgreSQL, Kafka, etc.)
- Usar DataStream API para lógica mais complexa

### Troubleshooting

**Erro: "Could not find a version of Java"**
```bash
java -version  # Verifica se Java está instalado
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64  # Ajustar path
```

**Erro: "ModuleNotFoundError: pyflink"**
```bash
source venv_py310/bin/activate  # Ativar venv correto
pip install apache-flink==1.18.1  # Reinstalar se necessário
```

**Download lento**
- Dataset é baixado de AWS CloudFront (~40MB)
- Alternativa: baixe manualmente de https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page



Exemplo de uso:

```bash
# Baixa e extrai Flink (não altera seu shell por padrão)
./setup.sh

# Inicia o cluster local
./start-flink.sh

# Acesse a UI em http://localhost:8081

# Parar o cluster
./stop-flink.sh
```

Requisitos mínimos:

- Java 11 ou superior
- `wget` ou `curl` para download

Próximos passos recomendados:

- Se você desenvolve em Java: criar um projeto Maven/Gradle que dependa de flink-runtime.
- Se preferir executar em container: criar `docker-compose.yml` com Flink + Zookeeper (opcional).
