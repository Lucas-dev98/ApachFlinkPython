# 🌐 Dashboard em Tempo Real - Guia de Uso

## 📊 O que é?

Dashboard HTML que se atualiza automaticamente conforme o pipeline Apache Flink processa os dados. Mostra resultados em tempo real sem precisar recarregar a página!

---

## 🚀 Como Usar

### Opção 1: Dois Terminais (Recomendado)

**Terminal 1 - Iniciar Dashboard:**
```bash
cd ~/apacheFlink
./start_dashboard.sh
```

Você verá:
```
════════════════════════════════════════════════════════════════
🌐 DASHBOARD EM TEMPO REAL INICIADO
════════════════════════════════════════════════════════════════

  📊 Dashboard URL:  http://localhost:8000
  🔌 API Status:     http://localhost:8000/api/status
  📈 API Results:    http://localhost:8000/api/results

════════════════════════════════════════════════════════════════
```

**Abra o dashboard no navegador:**
```bash
xdg-open http://localhost:8000
```

**Terminal 2 - Executar Pipeline:**
```bash
cd ~/apacheFlink
./run_pipeline.sh
```

✅ O dashboard irá atualizar automaticamente conforme o pipeline processa!

---

### Opção 2: Modo Background

**Iniciar servidor em background:**
```bash
cd ~/apacheFlink
nohup ./start_dashboard.sh > dashboard.log 2>&1 &
```

**Abrir dashboard:**
```bash
xdg-open http://localhost:8000
```

**Executar pipeline:**
```bash
./run_pipeline.sh
```

**Parar servidor depois:**
```bash
pkill -f dashboard_server
```

---

## 🎯 Recursos do Dashboard

### 1. Atualização Automática
- ⚡ **Atualiza a cada 2 segundos**
- 🔴 **Indicador "LIVE"** piscando
- 📅 **Timestamp** de última atualização

### 2. Cards de Estatísticas
- 📊 **Registros Processados** - Contador em tempo real
- ✅ **Análises Concluídas** - Progresso (0/3, 1/3, 2/3, 3/3)
- ⏱️ **Tempo de Execução** - Contador de tempo
- 🟢 **Status** - Aguardando / Em execução / Sucesso

### 3. Tabelas Dinâmicas
- **Top 10 Rotas** - Atualiza conforme dados chegam
- **Receita por Hora** - 24 linhas ordenadas
- **Distribuição por Distância** - 5 faixas de distância

### 4. Visualizações
- 📊 **Barras proporcionais** animadas
- 🎨 **Cores gradientes** (azul → roxo)
- 🖱️ **Hover effects** interativos

---

## 📡 API Endpoints

### GET /api/status
Retorna status da execução:
```json
{
  "timestamp": "2025-10-14T22:46:24",
  "execution_time_seconds": 36.1,
  "statistics": {
    "records_processed": 245455,
    "analyses_completed": 3,
    "errors": 0,
    "warnings": 0
  },
  "success": true
}
```

### GET /api/results
Retorna dados das análises:
```json
{
  "top_routes": [
    {"pickup_location": "237", "dropoff_location": "236", "trip_count": "1503"},
    ...
  ],
  "revenue_by_hour": [
    {"hour_of_day": "0", "total_trips": "8956", "total_revenue": "299126.78", "avg_fare": "23.67"},
    ...
  ],
  "trips_by_distance": [
    {"distance_range": "0-1 miles", "trip_count": "43686", "avg_fare": "7.60", "avg_duration_min": "1.4"},
    ...
  ]
}
```

---

## 🎬 Demonstração Completa

```bash
# Terminal 1: Servidor do dashboard
cd ~/apacheFlink
./start_dashboard.sh

# Aguarde mensagem:
# 📊 Dashboard URL:  http://localhost:8000

# Em outro terminal ou navegador:
xdg-open http://localhost:8000

# Terminal 2: Pipeline
cd ~/apacheFlink
source env.sh
source venv_py310/bin/activate
./start-flink.sh
python examples/pyflink_nyc_taxi_csv.py

# Observe o dashboard atualizando em tempo real! 🎉
```

---

## 🔧 Personalização

### Mudar intervalo de atualização

Edite `data/output/dashboard_live.html`:
```javascript
const UPDATE_INTERVAL = 5000; // 5 segundos (padrão: 2000)
```

### Mudar porta do servidor

```bash
python examples/dashboard_server.py 3000  # Porta 3000
```

Ou edite `start_dashboard.sh`:
```bash
python3 examples/dashboard_server.py 3000
```

---

## 🛠️ Troubleshooting

### ❌ "Address already in use"
```bash
# Porta 8000 já em uso, mude para outra porta:
python examples/dashboard_server.py 8001
```

### ❌ Dashboard não atualiza
1. Verifique se o servidor está rodando
2. Abra console do navegador (F12)
3. Veja erros na aba "Console"
4. Verifique se `execution_report.json` está sendo gerado

### ❌ "Cannot GET /api/status"
- Certifique-se de estar acessando `http://localhost:8000` (não `file://`)
- O servidor precisa estar rodando

### ❌ Dados não aparecem
```bash
# Verifique se os arquivos existem:
ls -la data/output/nyc_taxi_analysis/*/part-*

# Verifique o relatório:
cat data/output/nyc_taxi_analysis/execution_report.json
```

---

## 📊 Comparação: Dashboard Estático vs Tempo Real

### Dashboard Estático (`dashboard.html`)
- ✅ Simples de usar
- ✅ Funciona com `file://`
- ❌ Precisa recarregar para ver atualizações
- ❌ Não mostra progresso

### Dashboard Tempo Real (`dashboard_live.html`)
- ✅ Atualização automática
- ✅ Mostra progresso em tempo real
- ✅ API para integração
- ✅ Indicador "LIVE"
- ❌ Precisa de servidor HTTP
- ❌ Requer dois terminais

---

## 🎯 Casos de Uso

### Desenvolvimento
Use dashboard **tempo real** para:
- Debugar pipeline
- Ver resultados conforme são gerados
- Monitorar performance

### Produção/Apresentação
Use dashboard **estático** para:
- Compartilhar resultados finais
- Enviar por email (arquivo HTML único)
- Apresentações offline

---

## 📁 Arquivos

```
apacheFlink/
├── start_dashboard.sh          # Inicia servidor
├── examples/
│   └── dashboard_server.py     # Servidor HTTP + API
└── data/output/
    ├── dashboard.html          # Dashboard estático
    └── dashboard_live.html     # Dashboard tempo real
```

---

## 🚀 Quick Start (Copy & Paste)

```bash
# Terminal 1
cd ~/apacheFlink && ./start_dashboard.sh &
sleep 2 && xdg-open http://localhost:8000

# Terminal 2
cd ~/apacheFlink && \
source env.sh && \
source venv_py310/bin/activate && \
./start-flink.sh && \
python examples/pyflink_nyc_taxi_csv.py
```

---

## 📝 Notas

- **Atualização automática:** A cada 2 segundos via AJAX
- **Sem WebSocket:** Usa polling simples (mais compatível)
- **CORS habilitado:** Funciona com qualquer origem
- **CSV parsing:** Lê arquivos `part-*` diretamente
- **Fallback gracioso:** Mostra "Aguardando..." se sem dados

---

## 🎉 Resultado

Você terá um dashboard profissional que:
- 📊 Atualiza em tempo real
- 🎨 Visual moderno e interativo
- 📈 Mostra progresso da execução
- 🔴 Indicador "LIVE" piscando
- ⚡ API REST para integração

**Perfeito para demonstrações e monitoramento!** 🚀
