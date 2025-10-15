# Apache Flink + PyFlink - Big Data Pipeline# Apache Flink + PyFlink - Big Data Pipeline# apacheFlink — ambiente local de desenvolvimento



Projeto completo de processamento de Big Data usando **Apache Flink** e **PyFlink** com dataset real (NYC Taxi Trip Records).



## 📋 RequisitosProjeto completo de processamento de Big Data usando **Apache Flink** e **PyFlink** com dataset real (NYC Taxi Trip Records).Este diretório contém scripts para configurar um ambiente local de desenvolvimento com Apache Flink (binário).



- **Java 11+** (JDK instalado)

- **Python 3.10** (via pyenv)

- **Linux/macOS** (testado em Ubuntu)## 📋 RequisitosArquivos principais:



## 🚀 Início Rápido



### 1. Configurar Ambiente- **Java 11+** (JDK instalado)- `setup.sh` — baixa e extrai a distribuição binária do Flink (padrão: 1.18.1). Use `--set-env` para adicionar variáveis ao `~/.bashrc`.



```bash- **Python 3.10** (via pyenv)- `start-flink.sh` — inicia um cluster Flink local (jobmanager + taskmanager).

# Executar setup (baixa Flink e cria env.sh)

./setup.sh- **Linux/macOS** (testado em Ubuntu)- `stop-flink.sh` — para o cluster local.



# Carregar variáveis de ambiente

source env.sh

## 🚀 Início RápidoEnvironment file

# Ativar virtualenv Python

source venv_py310/bin/activate----------------

```

### 1. Configurar Ambiente

### 2. Iniciar Cluster Flink

After running `./setup.sh` the script will generate `env.sh` in the project root. This file contains:

```bash

./start-flink.sh```bash

```

# Executar setup (baixa Flink e cria env.sh)- `FLINK_HOME` and `PATH` entries pointing to the extracted Flink binary

**Acesse a UI:** http://localhost:8081

./setup.sh- If a Python virtualenv exists at `./venv`, `env.sh` will add the virtualenv `bin` to `PATH` and set `VIRTUAL_ENV`.

### 3. Executar Pipeline Big Data



```bash

# Pipeline NYC Taxi (3 análises de Big Data)# Carregar variáveis de ambienteYou can load it manually with:

python examples/pyflink_nyc_taxi_csv.py --download

```source env.sh



### 4. Parar Cluster```bash



```bash# Ativar virtualenv Pythonsource ./env.sh

./stop-flink.sh

```source venv_py310/bin/activate```



## 📁 Estrutura do Projeto```



```Or run `./setup.sh --set-env` to append a small `source ./env.sh` snippet to your `~/.bashrc`.

apacheFlink/

├── env.sh                      # Variáveis de ambiente### 2. Iniciar Cluster Flink

├── setup.sh                    # Instala Flink

├── start-flink.sh              # Inicia clusterVirtualenv (Python)

├── stop-flink.sh               # Para cluster

├── run_pipeline.sh             # Automação completa```bash--------------------

│

├── venv_py310/                 # Python 3.10 + PyFlink./start-flink.sh

│

├── flink/                      # Apache Flink 1.18.1```To create a Python virtual environment named `venv` and install PyFlink:

│   └── apache-flink-1.18.1/

│

├── examples/

│   ├── pyflink_topn.py        # Exemplo Top-N**Acesse a UI:** http://localhost:8081```bash

│   └── pyflink_nyc_taxi_csv.py # Pipeline Big Data

│python3 -m venv venv

└── data/                           

    ├── real/### 3. Executar Pipeline Big Datasource venv/bin/activate

    │   └── nyc_taxi_2023_01_filtered.csv

    └── output/pip install --upgrade pip

        └── nyc_taxi_analysis/

            ├── top_routes/```bashpip install apache-flink==1.18.1

            ├── revenue_by_hour/

            └── trips_by_distance/# Pipeline NYC Taxi (3 análises de Big Data)```

```

python examples/pyflink_nyc_taxi_csv.py --download

## 🚕 Pipeline Big Data: NYC Taxi

```The generated `env.sh` will automatically add `venv/bin` to `PATH` if `venv` exists.

**Dataset:** NYC Yellow Taxi Trip Records (Janeiro 2023)

- **Registros:** ~245,000 viagens

- **Tamanho:** ~50MB CSV

- **Fonte:** [NYC TLC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)### 4. Parar ClusterExemplos PyFlink



### Análises Implementadas================



#### 1️⃣ Top 10 Rotas Mais Populares```bash

Identifica as 10 combinações pickup/dropoff location mais frequentes.

./stop-flink.sh## 1. Exemplo Simples: Top-N Customers

**Colunas:**

- `pickup_location` - ID da zona de pickup```

- `dropoff_location` - ID da zona de dropoff

- `trip_count` - Número de viagens`examples/pyflink_topn.py` - demonstra um job batch básico usando Table API.



#### 2️⃣ Receita por Hora do Dia## 📁 Estrutura do ProjetoLê `data/sample_transactions.csv`, agrega por cliente e retorna top-N.

Agrega receita total e média por hora (0-23h).



**Colunas:**

- `hour_of_day` - Hora (0-23)```## 2. Pipeline Big Data: NYC Taxi Dataset (COMPLETO)

- `total_trips` - Total de viagens

- `total_revenue` - Receita totalapacheFlink/

- `avg_fare` - Tarifa média

├── env.sh                      # Variáveis de ambiente**🚕 `examples/pyflink_nyc_taxi.py`** - Pipeline completo com dados reais!

#### 3️⃣ Distribuição por Distância

Agrupa viagens por faixas: 0-1mi, 1-3mi, 3-5mi, 5-10mi, 10+mi.├── setup.sh                    # Instala Flink



**Colunas:**├── start-flink.sh              # Inicia cluster### Dataset

- `distance_range` - Faixa de distância

- `trip_count` - Total de viagens├── stop-flink.sh               # Para cluster- **Fonte**: NYC Taxi and Limousine Commission (TLC)

- `avg_fare` - Tarifa média

- `avg_duration_min` - Duração estimada (minutos)├── run_pipeline.sh             # Automação completa- **Tamanho**: ~40MB (1 mês de dados - Janeiro 2023)



### Executar│- **Registros**: ~3 milhões de viagens



```bash├── venv_py310/                 # Python 3.10 + PyFlink- **Formato**: Parquet (otimizado para análise)

# Com download automático

python examples/pyflink_nyc_taxi_csv.py --download│- **URL**: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page



# Usando dataset existente├── flink/                      # Apache Flink 1.18.1

python examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv

```│   └── apache-flink-1.18.1/### Análises Implementadas



### Resultados (com headers)│



Todos os CSVs incluem cabeçalhos descritivos:├── examples/O pipeline executa 4 análises completas:



```csv│   ├── pyflink_topn.py        # Exemplo Top-N

# top_routes.csv

pickup_location,dropoff_location,trip_count│   └── pyflink_nyc_taxi_csv.py # Pipeline Big Data1. **Top 10 Rotas Mais Populares**

237,236,1503

264,264,1295│   - Agrega viagens por pickup/dropoff location IDs

236,237,1276

...└── data/                              - Identifica os pares de localizações mais frequentes



# revenue_by_hour.csv    ├── real/   - Output: `data/output/nyc_taxi_analysis/top_routes/`

hour_of_day,total_trips,total_revenue,avg_fare

0,8956,299126.78,23.67    │   └── nyc_taxi_2023_01_filtered.csv

6,4819,163953.38,25.21

18,19567,560234.12,28.64    └── output/2. **Receita por Hora do Dia**

...

        └── nyc_taxi_analysis/   - Agrega receita total por hora (0-23)

# trips_by_distance.csv

distance_range,trip_count,avg_fare,avg_duration_min            ├── top_routes/   - Calcula média de tarifa por hora

0-1 miles,43686,7.60,1.37

1-3 miles,111306,12.18,3.55            ├── revenue_by_hour/   - Útil para entender padrões de demanda

10+ miles,29770,65.52,33.00

...            └── trips_by_distance/   - Output: `data/output/nyc_taxi_analysis/revenue_by_hour/`

```

```

## 📊 Exemplo Simples: Top-N

3. **Distância Média por Tipo de Pagamento**

```bash

python examples/pyflink_topn.py \## 🚕 Pipeline Big Data: NYC Taxi   - Agrupa por payment_type (1=Cartão, 2=Dinheiro, etc.)

    --input data/sample_transactions.csv \

    --top 5   - Compara distância e valor médio por tipo

```

**Dataset:** NYC Yellow Taxi Trip Records (Janeiro 2023)   - Output: `data/output/nyc_taxi_analysis/distance_by_payment/`

## 🔧 Como Funciona

- **Registros:** ~245,000 viagens

### Arquitetura

- **Tamanho:** ~50MB CSV4. **Análise de Gorjetas**

```

[CSV Dataset]- **Fonte:** [NYC TLC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)   - Segmenta viagens por faixa de valor (0-10, 10-20, 20-30, 30-50, 50+)

      ↓

[PyFlink Table API]   - Calcula gorjeta média e percentual por faixa

      ↓

[SQL Transformações]### Análises Implementadas   - Apenas pagamentos com cartão (dinheiro não registra gorjeta)

  - GROUP BY

  - Agregações   - Output: `data/output/nyc_taxi_analysis/tip_analysis/`

  - ORDER BY + LIMIT

      ↓#### 1️⃣ Top 10 Rotas Mais Populares

[CSV Output com Headers]

```Identifica as 10 combinações pickup/dropoff location mais frequentes.### Como Funciona (Arquitetura)



### Tecnologias



- **Apache Flink 1.18.1** - Motor distribuído#### 2️⃣ Receita por Hora do Dia```

- **PyFlink** - Python API (Table API + SQL)

- **CSV Connector** - Leitura/escrita filesystemAgrega receita total e média por hora (0-23h).[Dataset Parquet]



## 🛠️ Troubleshooting      ↓



### Java not found#### 3️⃣ Distribuição por Distância[PyFlink Table API - Source]

```bash

java -versionAgrupa viagens por faixas: 0-1mi, 1-3mi, 3-5mi, 5-10mi, 10+mi.      ↓

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

```[SQL Queries - Transformações]



### ModuleNotFoundError: pyflink### Executar  - GROUP BY

```bash

source venv_py310/bin/activate  - Agregações (COUNT, SUM, AVG)

pip install apache-flink==1.18.1

``````bash  - Window Functions (HOUR)



### Cluster não inicia# Com download automático  - Filtros e CASE statements

```bash

tail -f flink/apache-flink-1.18.1/log/*.logpython examples/pyflink_nyc_taxi_csv.py --download      ↓

./stop-flink.sh && ./start-flink.sh

```[Filesystem Sink - CSV Output]



### Resultados sem headers# Usando dataset existente      ↓

Os CSVs agora incluem headers automaticamente. Se não aparecerem:

```bashpython examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv[Resultados em data/output/]

# Limpar resultados anteriores

rm -rf data/output/nyc_taxi_analysis/*``````



# Executar novamente

python examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv

```### Resultados**Tecnologias utilizadas:**



## 📚 Documentação- PyFlink Table API (abstração SQL sobre DataStream)



- [Apache Flink](https://flink.apache.org/)```- Parquet Reader (formato columnar eficiente)

- [PyFlink Docs](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/)

- [Table API](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/)data/output/nyc_taxi_analysis/- Batch Processing Mode (para dados históricos)



## 🎯 Próximos Passos├── top_routes/part-*.csv- CSV Writer (resultados legíveis)



1. Adicionar análise de gorjetas├── revenue_by_hour/part-*.csv

2. Implementar streaming em tempo real

3. Deploy em cluster distribuído└── trips_by_distance/part-*.csv### Execução Automatizada

4. Integração com Kafka

```

## 📝 Changelog

**Opção 1: Script Completo (Recomendado)**

### v1.1.0 (2025-10-14)

- ✨ Adicionados headers descritivos em todos os CSVs de resultado## 📊 Exemplo Simples: Top-N

- 🧹 Limpeza de arquivos temporários e desnecessários

- 📝 Documentação melhorada com exemplos de saída```bash



### v1.0.0 (2025-10-14)```bashchmod +x run_pipeline.sh

- 🎉 Release inicial

- ✅ Pipeline Big Data com NYC Taxi datasetpython examples/pyflink_topn.py \./run_pipeline.sh

- ✅ 3 análises completas com resultados

- ✅ Scripts de automação    --input data/sample_transactions.csv \```



---    --top 5



**Desenvolvido com** ⚡ Apache Flink + 🐍 PyFlink```O script `run_pipeline.sh` faz tudo automaticamente:


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
