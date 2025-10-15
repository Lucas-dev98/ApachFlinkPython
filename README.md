# 🚕 Apache Flink + PyFlink - Pipeline Big Data NYC Taxi# Apache Flink + PyFlink - Big Data Pipeline# Apache Flink + PyFlink - Big Data Pipeline# apacheFlink — ambiente local de desenvolvimento



Projeto completo de processamento de Big Data usando **Apache Flink 1.18.1** e **PyFlink** com dataset real do NYC Yellow Taxi Trip Records.



[![GitHub](https://img.shields.io/badge/GitHub-ApachFlinkPython-blue)](https://github.com/Lucas-dev98/ApachFlinkPython)Projeto completo de processamento de Big Data usando **Apache Flink** e **PyFlink** com dataset real (NYC Taxi Trip Records).

[![Python](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/)

[![Flink](https://img.shields.io/badge/Flink-1.18.1-orange)](https://flink.apache.org/)



---## 📋 RequisitosProjeto completo de processamento de Big Data usando **Apache Flink** e **PyFlink** com dataset real (NYC Taxi Trip Records).Este diretório contém scripts para configurar um ambiente local de desenvolvimento com Apache Flink (binário).



## 📋 Índice



- [Requisitos](#-requisitos)- **Java 11+** (JDK instalado)

- [Instalação Rápida](#-instalação-rápida)

- [Como Executar](#-como-executar)- **Python 3.10** (via pyenv)

- [Interface de Progresso](#-interface-de-progresso-v120)

- [Análises Implementadas](#-análises-implementadas)- **Linux/macOS** (testado em Ubuntu)## 📋 RequisitosArquivos principais:

- [Estrutura do Projeto](#-estrutura-do-projeto)

- [Dashboard HTML](#-dashboard-html)

- [Troubleshooting](#-troubleshooting)

- [Documentação](#-documentação)## 🚀 Início Rápido



---



## 📋 Requisitos### 1. Configurar Ambiente- **Java 11+** (JDK instalado)- `setup.sh` — baixa e extrai a distribuição binária do Flink (padrão: 1.18.1). Use `--set-env` para adicionar variáveis ao `~/.bashrc`.



- **Java 11+** (OpenJDK ou Oracle)

- **Python 3.10** (via pyenv ou sistema)

- **Linux/macOS** (testado em Ubuntu 22.04)```bash- **Python 3.10** (via pyenv)- `start-flink.sh` — inicia um cluster Flink local (jobmanager + taskmanager).

- **4GB RAM** mínimo

- **2GB espaço em disco** (Flink + dataset)# Executar setup (baixa Flink e cria env.sh)



---./setup.sh- **Linux/macOS** (testado em Ubuntu)- `stop-flink.sh` — para o cluster local.



## 🚀 Instalação Rápida



### 1. Clone o Repositório# Carregar variáveis de ambiente



```bashsource env.sh

git clone git@github.com:Lucas-dev98/ApachFlinkPython.git

cd ApachFlinkPython## 🚀 Início RápidoEnvironment file

```

# Ativar virtualenv Python

### 2. Execute o Setup

source venv_py310/bin/activate----------------

```bash

# Instala Flink, cria ambiente Python e configura tudo automaticamente```

./setup.sh

```### 1. Configurar Ambiente



### 3. Ative o Ambiente### 2. Iniciar Cluster Flink



```bashAfter running `./setup.sh` the script will generate `env.sh` in the project root. This file contains:

# Carregar variáveis de ambiente

source env.sh```bash



# Ativar virtualenv Python./start-flink.sh```bash

source venv_py310/bin/activate

``````



---# Executar setup (baixa Flink e cria env.sh)- `FLINK_HOME` and `PATH` entries pointing to the extracted Flink binary



## 🎯 Como Executar**Acesse a UI:** http://localhost:8081



### Opção 1: Script Automatizado (Recomendado) ⭐./setup.sh- If a Python virtualenv exists at `./venv`, `env.sh` will add the virtualenv `bin` to `PATH` and set `VIRTUAL_ENV`.



**Executa tudo automaticamente: setup, cluster, pipeline e dashboard!**### 3. Executar Pipeline Big Data



```bash

./run_pipeline.sh

``````bash



Esse script faz:# Pipeline NYC Taxi (3 análises de Big Data)# Carregar variáveis de ambienteYou can load it manually with:

- ✅ Ativa ambiente Python (pyenv + venv)

- ✅ Verifica/instala Flink se necessáriopython examples/pyflink_nyc_taxi_csv.py --download

- ✅ Inicia cluster local (JobManager + TaskManager)

- ✅ Executa pipeline com interface de progresso```source env.sh

- ✅ Gera dashboard HTML interativo

- ✅ Exibe preview dos resultados

- ✅ Para o cluster ao final

### 4. Parar Cluster```bash

---



### Opção 2: Execução Manual Passo a Passo

```bash# Ativar virtualenv Pythonsource ./env.sh

#### Passo 1: Ativar Ambiente

./stop-flink.sh

```bash

# Carregar variáveis de ambiente do Flink```source venv_py310/bin/activate```

source env.sh



# Ativar virtualenv Python 3.10

source venv_py310/bin/activate## 📁 Estrutura do Projeto```

```



#### Passo 2: Iniciar Cluster Flink

```Or run `./setup.sh --set-env` to append a small `source ./env.sh` snippet to your `~/.bashrc`.

```bash

# Inicia JobManager + TaskManager localapacheFlink/

./start-flink.sh

├── env.sh                      # Variáveis de ambiente### 2. Iniciar Cluster Flink

# Verificar se está rodando

jps  # Deve mostrar: StandaloneSessionClusterEntrypoint, TaskManagerRunner├── setup.sh                    # Instala Flink



# Acessar WebUI (opcional)├── start-flink.sh              # Inicia clusterVirtualenv (Python)

xdg-open http://localhost:8081

```├── stop-flink.sh               # Para cluster



#### Passo 3: Executar Pipeline├── run_pipeline.sh             # Automação completa```bash--------------------



**Com interface de progresso (padrão):**│

```bash

python examples/pyflink_nyc_taxi_csv.py├── venv_py310/                 # Python 3.10 + PyFlink./start-flink.sh

```

│

**Com download automático do dataset:**

```bash├── flink/                      # Apache Flink 1.18.1```To create a Python virtual environment named `venv` and install PyFlink:

python examples/pyflink_nyc_taxi_csv.py --download

```│   └── apache-flink-1.18.1/



**Sem interface de progresso:**│

```bash

python examples/pyflink_nyc_taxi_csv.py --no-progress├── examples/

```

│   ├── pyflink_topn.py        # Exemplo Top-N**Acesse a UI:** http://localhost:8081```bash

**Com dataset customizado:**

```bash│   └── pyflink_nyc_taxi_csv.py # Pipeline Big Data

python examples/pyflink_nyc_taxi_csv.py --data /caminho/para/seu_dataset.csv

```│python3 -m venv venv



**Com diretório de saída customizado:**└── data/                           

```bash

python examples/pyflink_nyc_taxi_csv.py --output meu_diretorio/resultados    ├── real/### 3. Executar Pipeline Big Datasource venv/bin/activate

```

    │   └── nyc_taxi_2023_01_filtered.csv

#### Passo 4: Gerar Dashboard HTML

    └── output/pip install --upgrade pip

```bash

python examples/generate_dashboard.py data/output/nyc_taxi_analysis        └── nyc_taxi_analysis/



# Abrir no navegador            ├── top_routes/```bashpip install apache-flink==1.18.1

xdg-open data/output/dashboard.html

```            ├── revenue_by_hour/



#### Passo 5: Parar Cluster            └── trips_by_distance/# Pipeline NYC Taxi (3 análises de Big Data)```



```bash```

./stop-flink.sh

```python examples/pyflink_nyc_taxi_csv.py --download



---## 🚕 Pipeline Big Data: NYC Taxi



### Opção 3: Comandos Individuais```The generated `env.sh` will automatically add `venv/bin` to `PATH` if `venv` exists.



#### Apenas Download do Dataset**Dataset:** NYC Yellow Taxi Trip Records (Janeiro 2023)



```bash- **Registros:** ~245,000 viagens

source env.sh

source venv_py310/bin/activate- **Tamanho:** ~50MB CSV

python examples/pyflink_nyc_taxi_csv.py --download

# Dataset salvo em: data/real/nyc_taxi_2023_01_filtered.csv- **Fonte:** [NYC TLC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)### 4. Parar ClusterExemplos PyFlink

```



#### Apenas Gerar Dashboard

### Análises Implementadas================

```bash

python examples/generate_dashboard.py data/output/nyc_taxi_analysis

```

#### 1️⃣ Top 10 Rotas Mais Populares```bash

#### Ver Resultados no Terminal

Identifica as 10 combinações pickup/dropoff location mais frequentes.

```bash

# Top 10 Rotas./stop-flink.sh## 1. Exemplo Simples: Top-N Customers

head -20 data/output/nyc_taxi_analysis/top_routes/part-*

**Colunas:**

# Receita por Hora

head -30 data/output/nyc_taxi_analysis/revenue_by_hour/part-*- `pickup_location` - ID da zona de pickup```



# Distribuição por Distância- `dropoff_location` - ID da zona de dropoff

head -10 data/output/nyc_taxi_analysis/trips_by_distance/part-*

```- `trip_count` - Número de viagens`examples/pyflink_topn.py` - demonstra um job batch básico usando Table API.



#### Limpar Resultados Anteriores



```bash#### 2️⃣ Receita por Hora do Dia## 📁 Estrutura do ProjetoLê `data/sample_transactions.csv`, agrega por cliente e retorna top-N.

rm -rf data/output/nyc_taxi_analysis/*

rm -f data/output/dashboard.htmlAgrega receita total e média por hora (0-23h).

```



---

**Colunas:**

## 🎨 Interface de Progresso (v1.2.0)

- `hour_of_day` - Hora (0-23)```## 2. Pipeline Big Data: NYC Taxi Dataset (COMPLETO)

### Recursos da Interface

- `total_trips` - Total de viagens

A versão 1.2.0 inclui interface completa de acompanhamento:

- `total_revenue` - Receita totalapacheFlink/

- ✅ **Barra de progresso animada** com estimativa de tempo (ETA)

- 🎨 **Logging colorido** (verde/vermelho/amarelo/azul/cyan)- `avg_fare` - Tarifa média

- 📊 **Estatísticas em tempo real** (registros, tempo, throughput)

- 📝 **Relatório JSON automático** (execution_report.json)├── env.sh                      # Variáveis de ambiente**🚕 `examples/pyflink_nyc_taxi.py`** - Pipeline completo com dados reais!

- 🌐 **Dashboard HTML interativo** com visualizações

#### 3️⃣ Distribuição por Distância

### Exemplo de Output

Agrupa viagens por faixas: 0-1mi, 1-3mi, 3-5mi, 5-10mi, 10+mi.├── setup.sh                    # Instala Flink

```

================================================================================

                 🚕 PyFlink Big Data Pipeline - NYC Taxi Dataset                 

================================================================================**Colunas:**├── start-flink.sh              # Inicia cluster### Dataset



- `distance_range` - Faixa de distância

  ✓ [22:22:15] Usando dataset existente: data/real/nyc_taxi_2023_01_filtered.csv

- `trip_count` - Total de viagens├── stop-flink.sh               # Para cluster- **Fonte**: NYC Taxi and Limousine Commission (TLC)

▶ Configuração do Ambiente

  Inicializando Apache Flink em modo batch...- `avg_fare` - Tarifa média

  [████████████████░░░░░░░░░░░░] 30.0% | ETA: 18.1s | Criando tabela fonte

  ✓ Ambiente Flink configurado- `avg_duration_min` - Duração estimada (minutos)├── run_pipeline.sh             # Automação completa- **Tamanho**: ~40MB (1 mês de dados - Janeiro 2023)

  ✓ Tabela 'taxi_trips' criada



▶ Execução das Análises

  [█████████████████████████████████░░░] 75.0% | ETA: 9.6s | Análise 2 concluída### Executar│- **Registros**: ~3 milhões de viagens

  ✓ Análise 'Receita por Hora' finalizada

    📊 Resultados: 24 linhas



 ✓ PIPELINE CONCLUÍDA COM SUCESSO ```bash├── venv_py310/                 # Python 3.10 + PyFlink- **Formato**: Parquet (otimizado para análise)



────────────────────────────────────────────────────────────────────────────────# Com download automático

📊 ESTATÍSTICAS FINAIS

────────────────────────────────────────────────────────────────────────────────python examples/pyflink_nyc_taxi_csv.py --download│- **URL**: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page



  ⏱️  Tempo Total.........................                33.8s

  📝 Registros Processados.................             245,455

  ✅ Análises Concluídas...................                    3# Usando dataset existente├── flink/                      # Apache Flink 1.18.1

  ⚡ Throughput...........................            7,262.4 rec/s

```python examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv



Para desabilitar a interface:```│   └── apache-flink-1.18.1/### Análises Implementadas

```bash

python examples/pyflink_nyc_taxi_csv.py --no-progress

```

### Resultados (com headers)│

---



## 📊 Análises Implementadas

Todos os CSVs incluem cabeçalhos descritivos:├── examples/O pipeline executa 4 análises completas:

### 1️⃣ Top 10 Rotas Mais Populares



Identifica as 10 combinações de pickup/dropoff location mais frequentes.

```csv│   ├── pyflink_topn.py        # Exemplo Top-N

**Colunas de saída:**

- `pickup_location` - ID da zona de embarque# top_routes.csv

- `dropoff_location` - ID da zona de desembarque

- `trip_count` - Número de viagenspickup_location,dropoff_location,trip_count│   └── pyflink_nyc_taxi_csv.py # Pipeline Big Data1. **Top 10 Rotas Mais Populares**



**Arquivo:** `data/output/nyc_taxi_analysis/top_routes/part-*`237,236,1503



### 2️⃣ Receita por Hora do Dia264,264,1295│   - Agrega viagens por pickup/dropoff location IDs



Agrega receita total e média por cada hora (0-23h).236,237,1276



**Colunas de saída:**...└── data/                              - Identifica os pares de localizações mais frequentes

- `hour_of_day` - Hora do dia (0-23)

- `total_trips` - Total de viagens

- `total_revenue` - Receita total ($)

- `avg_fare` - Tarifa média ($)# revenue_by_hour.csv    ├── real/   - Output: `data/output/nyc_taxi_analysis/top_routes/`



**Arquivo:** `data/output/nyc_taxi_analysis/revenue_by_hour/part-*`hour_of_day,total_trips,total_revenue,avg_fare



### 3️⃣ Distribuição por Distância0,8956,299126.78,23.67    │   └── nyc_taxi_2023_01_filtered.csv



Agrupa viagens por faixas: 0-1mi, 1-3mi, 3-5mi, 5-10mi, 10+mi.6,4819,163953.38,25.21



**Colunas de saída:**18,19567,560234.12,28.64    └── output/2. **Receita por Hora do Dia**

- `distance_range` - Faixa de distância

- `trip_count` - Total de viagens...

- `avg_fare` - Tarifa média ($)

- `avg_duration_min` - Duração estimada (minutos)        └── nyc_taxi_analysis/   - Agrega receita total por hora (0-23)



**Arquivo:** `data/output/nyc_taxi_analysis/trips_by_distance/part-*`# trips_by_distance.csv



---distance_range,trip_count,avg_fare,avg_duration_min            ├── top_routes/   - Calcula média de tarifa por hora



## 📁 Estrutura do Projeto0-1 miles,43686,7.60,1.37



```1-3 miles,111306,12.18,3.55            ├── revenue_by_hour/   - Útil para entender padrões de demanda

ApachFlinkPython/

├── README.md                       # Documentação principal (você está aqui!)10+ miles,29770,65.52,33.00

├── INTERFACE_DOCS.md               # Documentação da interface de progresso

├── INTERFACE_RELEASE.md            # Release notes da v1.2.0...            └── trips_by_distance/   - Output: `data/output/nyc_taxi_analysis/revenue_by_hour/`

├── RESUMO_FINAL.txt               # Resumo em português do projeto

├── COMANDOS.sh                    # Quick reference de comandos```

│

├── setup.sh                       # ⚙️  Script de instalação completa```

├── run_pipeline.sh                # 🚀 Execução automatizada (USAR ESTE!)

├── start-flink.sh                 # ▶️  Inicia cluster Flink local## 📊 Exemplo Simples: Top-N

├── stop-flink.sh                  # ⏹️  Para cluster Flink

├── env.sh                         # 📝 Variáveis de ambiente (gerado)3. **Distância Média por Tipo de Pagamento**

│

├── venv_py310/                    # 🐍 Python 3.10 + PyFlink```bash

│   ├── bin/

│   ├── lib/python examples/pyflink_topn.py \## 🚕 Pipeline Big Data: NYC Taxi   - Agrupa por payment_type (1=Cartão, 2=Dinheiro, etc.)

│   └── ...

│    --input data/sample_transactions.csv \

├── flink/                         # ⚡ Apache Flink 1.18.1 (binário)

│   └── apache-flink-1.18.1/    --top 5   - Compara distância e valor médio por tipo

│       ├── bin/                   # Executáveis do Flink

│       ├── conf/                  # Configurações```

│       ├── lib/                   # JARs do Flink

│       └── log/                   # Logs de execução**Dataset:** NYC Yellow Taxi Trip Records (Janeiro 2023)   - Output: `data/output/nyc_taxi_analysis/distance_by_payment/`

│

├── examples/                      # 📊 Scripts Python## 🔧 Como Funciona

│   ├── pyflink_topn.py           # Exemplo simples Top-N

│   ├── pyflink_nyc_taxi_csv.py   # 🚕 Pipeline principal (EXECUTAR ESTE!)- **Registros:** ~245,000 viagens

│   ├── progress_tracker.py        # 🎨 Classe de interface de progresso

│   └── generate_dashboard.py      # 🌐 Gerador de dashboard HTML### Arquitetura

│

└── data/                          # 💾 Dados e resultados- **Tamanho:** ~50MB CSV4. **Análise de Gorjetas**

    ├── sample_transactions.csv    # Dataset de exemplo

    ├── real/```

    │   └── nyc_taxi_2023_01_filtered.csv  # Dataset NYC (245K registros)

    └── output/[CSV Dataset]- **Fonte:** [NYC TLC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)   - Segmenta viagens por faixa de valor (0-10, 10-20, 20-30, 30-50, 50+)

        ├── dashboard.html         # 🌐 Dashboard interativo (ABRIR ESTE!)

        └── nyc_taxi_analysis/      ↓

            ├── execution_report.json      # Relatório de execução

            ├── top_routes/                # Top 10 rotas[PyFlink Table API]   - Calcula gorjeta média e percentual por faixa

            ├── revenue_by_hour/           # Receita por hora

            └── trips_by_distance/         # Distribuição por distância      ↓

```

[SQL Transformações]### Análises Implementadas   - Apenas pagamentos com cartão (dinheiro não registra gorjeta)

---

  - GROUP BY

## 🌐 Dashboard HTML

  - Agregações   - Output: `data/output/nyc_taxi_analysis/tip_analysis/`

O dashboard HTML é gerado automaticamente e inclui:

  - ORDER BY + LIMIT

### Visualizações

      ↓#### 1️⃣ Top 10 Rotas Mais Populares

- 📊 **Cards de Estatísticas**

  - Registros processados[CSV Output com Headers]

  - Análises concluídas

  - Tempo de execução```Identifica as 10 combinações pickup/dropoff location mais frequentes.### Como Funciona (Arquitetura)

  - Status (sucesso/avisos)



- 📈 **Tabelas Interativas**

  - Top 10 Rotas com barras visuais### Tecnologias

  - Receita por Hora do Dia

  - Distribuição por Distância



### Como Abrir- **Apache Flink 1.18.1** - Motor distribuído#### 2️⃣ Receita por Hora do Dia```



```bash- **PyFlink** - Python API (Table API + SQL)

# Opção 1: Abrir automaticamente

xdg-open data/output/dashboard.html- **CSV Connector** - Leitura/escrita filesystemAgrega receita total e média por hora (0-23h).[Dataset Parquet]



# Opção 2: Copiar link e colar no navegador

echo "file://$(pwd)/data/output/dashboard.html"

## 🛠️ Troubleshooting      ↓

# Opção 3: No Windows (WSL)

explorer.exe data/output/dashboard.html

```

### Java not found#### 3️⃣ Distribuição por Distância[PyFlink Table API - Source]

---

```bash

## 🛠️ Troubleshooting

java -versionAgrupa viagens por faixas: 0-1mi, 1-3mi, 3-5mi, 5-10mi, 10+mi.      ↓

### ❌ "bash: ./run_pipeline.sh: Permission denied"

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

```bash

chmod +x run_pipeline.sh setup.sh start-flink.sh stop-flink.sh```[SQL Queries - Transformações]

```



### ❌ "java: command not found"

### ModuleNotFoundError: pyflink### Executar  - GROUP BY

```bash

# Verificar se Java está instalado```bash

java -version

source venv_py310/bin/activate  - Agregações (COUNT, SUM, AVG)

# Se não estiver, instalar:

sudo apt updatepip install apache-flink==1.18.1

sudo apt install openjdk-11-jdk

``````bash  - Window Functions (HOUR)

# Configurar JAVA_HOME

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

```

### Cluster não inicia# Com download automático  - Filtros e CASE statements

### ❌ "ModuleNotFoundError: No module named 'pyflink'"

```bash

```bash

# Ativar o virtualenv corretotail -f flink/apache-flink-1.18.1/log/*.logpython examples/pyflink_nyc_taxi_csv.py --download      ↓

source venv_py310/bin/activate

./stop-flink.sh && ./start-flink.sh

# Verificar se PyFlink está instalado

pip list | grep apache-flink```[Filesystem Sink - CSV Output]



# Se não estiver, instalar:

pip install apache-flink==1.18.1

```### Resultados sem headers# Usando dataset existente      ↓



### ❌ "Address already in use (8081)"Os CSVs agora incluem headers automaticamente. Se não aparecerem:



```bash```bashpython examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv[Resultados em data/output/]

# Parar cluster Flink

./stop-flink.sh# Limpar resultados anteriores



# Matar processos do Flink se necessáriorm -rf data/output/nyc_taxi_analysis/*``````

pkill -f flink



# Iniciar novamente

./start-flink.sh# Executar novamente

```

python examples/pyflink_nyc_taxi_csv.py --data data/real/nyc_taxi_2023_01_filtered.csv

### ❌ Dataset não encontrado

```### Resultados**Tecnologias utilizadas:**

```bash

# Baixar dataset automaticamente

python examples/pyflink_nyc_taxi_csv.py --download

```## 📚 Documentação- PyFlink Table API (abstração SQL sobre DataStream)



### 🔍 Logs e Debugging



```bash- [Apache Flink](https://flink.apache.org/)```- Parquet Reader (formato columnar eficiente)

# Ver logs do JobManager

tail -f flink/apache-flink-1.18.1/log/flink-*-standalonesession-*.log- [PyFlink Docs](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/)



# Ver logs do TaskManager- [Table API](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/)data/output/nyc_taxi_analysis/- Batch Processing Mode (para dados históricos)

tail -f flink/apache-flink-1.18.1/log/flink-*-taskexecutor-*.log



# Acessar Flink WebUI para monitoramento

xdg-open http://localhost:8081## 🎯 Próximos Passos├── top_routes/part-*.csv- CSV Writer (resultados legíveis)

```



---

1. Adicionar análise de gorjetas├── revenue_by_hour/part-*.csv

## 📚 Documentação

2. Implementar streaming em tempo real

### Arquivos de Documentação

3. Deploy em cluster distribuído└── trips_by_distance/part-*.csv### Execução Automatizada

- **README.md** (este arquivo) - Guia completo de uso

- **INTERFACE_DOCS.md** - Documentação da interface de progresso4. Integração com Kafka

- **INTERFACE_RELEASE.md** - Release notes da versão 1.2.0

- **RESUMO_FINAL.txt** - Resumo do projeto em português```

- **COMANDOS.sh** - Quick reference de comandos úteis

## 📝 Changelog

### Links Externos

**Opção 1: Script Completo (Recomendado)**

- [Apache Flink Docs](https://flink.apache.org/docs/stable/)

- [PyFlink Docs](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/)### v1.1.0 (2025-10-14)

- [Flink Table API](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/tableapi/)

- [NYC TLC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)- ✨ Adicionados headers descritivos em todos os CSVs de resultado## 📊 Exemplo Simples: Top-N



### Dataset- 🧹 Limpeza de arquivos temporários e desnecessários



- **Fonte:** NYC Taxi & Limousine Commission (TLC)- 📝 Documentação melhorada com exemplos de saída```bash

- **URL:** https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

- **Período:** Janeiro 2023

- **Registros:** ~245,455 viagens

- **Tamanho:** ~50MB CSV filtrado (10 colunas)### v1.0.0 (2025-10-14)```bashchmod +x run_pipeline.sh



---- 🎉 Release inicial



## 🎯 Próximos Passos- ✅ Pipeline Big Data com NYC Taxi datasetpython examples/pyflink_topn.py \./run_pipeline.sh



### Para Aprender Mais- ✅ 3 análises completas com resultados



1. **Modificar análises SQL**: Edite `examples/pyflink_nyc_taxi_csv.py`- ✅ Scripts de automação    --input data/sample_transactions.csv \```

2. **Adicionar novas análises**: Siga o padrão das funções `analysis_X()`

3. **Processar mais dados**: Baixe múltiplos meses do dataset

4. **Implementar streaming**: Use DataStream API para dados em tempo real

5. **Deploy distribuído**: Configure cluster multi-node---    --top 5



### Ideias de Novas Análises



- Análise de gorjetas por tipo de pagamento**Desenvolvido com** ⚡ Apache Flink + 🐍 PyFlink```O script `run_pipeline.sh` faz tudo automaticamente:

- Padrões de demanda por dia da semana

- Correlação entre distância e gorjeta

- Zonas mais lucrativas por hora- ✓ Ativa ambiente Python (pyenv + venv)

- Tempo médio de viagem por região

## 🔧 Como Funciona- ✓ Verifica/instala Flink

---

- ✓ Inicia cluster local

## 📝 Changelog

### Arquitetura- ✓ Baixa dataset (~40MB download)

### v1.2.0 (2025-10-14)

- ✨ Adicionada interface completa de acompanhamento de execução- ✓ Executa todas as 4 análises

- 🎨 Implementado ProgressTracker com logging colorido

- 📊 Gerador de dashboard HTML interativo```- ✓ Salva resultados

- 📝 Relatório JSON automático de cada execução

- 🚀 Atualizado run_pipeline.sh com geração automática de dashboard[CSV Dataset]- ✓ Mostra preview dos resultados



### v1.1.0 (2025-10-14)      ↓

- ✨ Adicionados headers descritivos em todos os CSVs de resultado

- 🧹 Limpeza de arquivos temporários e desnecessários[PyFlink Table API]**Opção 2: Passo a Passo Manual**

- 📝 README reescrito com formatação correta

      ↓

### v1.0.0 (2025-10-14)

- 🎉 Release inicial do projeto[SQL Transformações]```bash

- ✅ Pipeline Big Data com NYC Taxi dataset (245K registros)

- ✅ 3 análises completas implementadas  - GROUP BY# 1. Ativar ambiente

- ✅ Scripts de automação completos

  - Agregaçõessource venv_py310/bin/activate

---

  - ORDER BY + LIMITsource env.sh

## 👤 Autor

      ↓

**Lucas Bastos**

- GitHub: [@Lucas-dev98](https://github.com/Lucas-dev98)[CSV Output]# 2. Baixar Flink (se necessário)

- Email: l.o.bastos@live.com

```./setup.sh

---



## ⭐ GitHub

### Tecnologias# 3. Iniciar cluster

Se este projeto foi útil para você, considere dar uma ⭐ no repositório!

./start-flink.sh

**🔗 https://github.com/Lucas-dev98/ApachFlinkPython**

- **Apache Flink 1.18.1** - Motor distribuído

---

- **PyFlink** - Python API (Table API + SQL)# 4. Executar pipeline

**Desenvolvido com** ⚡ Apache Flink + 🐍 PyFlink + ❤️

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
