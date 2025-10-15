# Interface de Acompanhamento de Execução 🎯

## Visão Geral

A interface de acompanhamento foi implementada para fornecer **feedback visual em tempo real** durante a execução do pipeline PyFlink. Ela inclui:

- ✅ **Barra de progresso** animada com estimativa de tempo
- 🎨 **Logging colorido** com níveis hierárquicos
- 📊 **Estatísticas detalhadas** ao final da execução
- 📝 **Relatório JSON** automático
- 🌐 **Dashboard HTML** interativo

---

## Componentes

### 1. ProgressTracker (`progress_tracker.py`)

Classe principal que gerencia o tracking de progresso:

```python
from progress_tracker import ProgressTracker

tracker = ProgressTracker(total_steps=100)
tracker.start("Minha Pipeline")

# Fases do processamento
tracker.start_phase("Download", "Baixando dados...")
tracker.complete_phase(records_count=10000)

# Barra de progresso
tracker.update_progress(50, "Processando dados...")

# Logs coloridos
tracker.log_info("Informação geral")
tracker.log_success("Operação bem-sucedida")
tracker.log_warning("Atenção necessária")
tracker.log_error("Erro encontrado")

# Finalização
tracker.finish(success=True)
```

#### Recursos:
- **Cores ANSI**: Verde (sucesso), Vermelho (erro), Amarelo (aviso), Azul (info)
- **Timestamps**: Opcional em cada log
- **Barra de progresso**: Com percentual e ETA (tempo estimado)
- **Estatísticas**: Registros processados, análises concluídas, erros, avisos
- **Throughput**: Registros por segundo calculado automaticamente

---

### 2. Dashboard HTML (`generate_dashboard.py`)

Gerador de dashboard interativo com visualizações:

```bash
python examples/generate_dashboard.py data/output/nyc_taxi_analysis
```

#### Características:
- 📊 **Cards de estatísticas**: Registros processados, tempo de execução, status
- 📈 **Tabelas interativas**: Com barras de visualização proporcionais
- 🎨 **Design moderno**: Gradiente roxo, sombras, hover effects
- 📱 **Responsivo**: Adapta-se a diferentes tamanhos de tela
- 🔄 **Auto-refresh**: Dados carregados dos CSVs e relatório JSON

#### Seções do Dashboard:
1. **Header**: Título e estatísticas gerais
2. **Top 10 Rotas**: Viagens mais populares
3. **Receita por Hora**: Distribuição ao longo do dia
4. **Viagens por Distância**: Análise por faixas

---

## Uso no Pipeline

### Execução Padrão (com interface):
```bash
./run_pipeline.sh
# ou
python examples/pyflink_nyc_taxi_csv.py
```

### Execução Sem Interface:
```bash
python examples/pyflink_nyc_taxi_csv.py --no-progress
```

### Apenas Gerar Dashboard:
```bash
python examples/generate_dashboard.py data/output/nyc_taxi_analysis
```

---

## Exemplo de Output

```
================================================================================
                 🚕 PyFlink Big Data Pipeline - NYC Taxi Dataset                 
================================================================================

▶ Configuração do Ambiente
  Inicializando Apache Flink em modo batch...
  [22:22:15]
  [████████████████░░░░░░░░░░░░░░░░░░░░] 30.0% | ETA: 12.3s | Criando tabela fonte
  ✓ [22:22:22] Ambiente Flink configurado
  ✓ [22:22:23] Fase 'Configuração do Ambiente' concluída

▶ Execução das Análises
  Processando 3 análises de Big Data...
  [████████████████████████████░░░░░░░░] 55.0% | ETA: 18.5s | Análise 1 concluída
  ✓ [22:22:37] Análise 'Top 10 Rotas' finalizada
    📊 Resultados: 10 linhas
    📁 Arquivo: data/output/nyc_taxi_analysis/top_routes

...

 ✓ PIPELINE CONCLUÍDA COM SUCESSO 

────────────────────────────────────────────────────────────────────────────────
📊 ESTATÍSTICAS FINAIS
────────────────────────────────────────────────────────────────────────────────

  ⏱️  Tempo Total.........................                33.8s
  📝 Registros Processados.................             245,455
  ✅ Análises Concluídas...................                    3
  ⚠️  Avisos..............................                    0
  ❌ Erros.................................                    0
  ⚡ Throughput...........................            7,262.4 rec/s

────────────────────────────────────────────────────────────────────────────────
```

---

## Arquivos Gerados

### 1. Relatório JSON (`execution_report.json`)
```json
{
  "timestamp": "2025-10-14T22:22:48.123456",
  "execution_time_seconds": 33.8,
  "statistics": {
    "records_processed": 245455,
    "analyses_completed": 3,
    "errors": 0,
    "warnings": 0
  },
  "success": true
}
```

### 2. Dashboard HTML (`dashboard.html`)
- Arquivo HTML standalone (sem dependências externas)
- CSS inline para estilização
- Visualizações dinâmicas baseadas nos dados
- Pronto para ser aberto em qualquer navegador

---

## Personalização

### Cores Customizadas
Edite a classe `Colors` em `progress_tracker.py`:
```python
class Colors:
    GREEN = '\033[92m'  # Altere o código ANSI
    BLUE = '\033[94m'
    # ...
```

### Dashboard Styling
Edite o CSS inline em `generate_dashboard.py`:
```python
html = f"""
<style>
    body {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        /* Personalize aqui */
    }}
</style>
"""
```

---

## Benefícios

1. **Visibilidade**: Acompanhe em tempo real o progresso da pipeline
2. **Debugging**: Identifique rapidamente problemas com logs coloridos
3. **Métricas**: Estatísticas detalhadas ao final da execução
4. **Relatórios**: Documentação automática de cada execução
5. **Apresentação**: Dashboard HTML pronto para compartilhar resultados

---

## Compatibilidade

- ✅ Linux / macOS (cores ANSI funcionam nativamente)
- ✅ Windows Terminal / Windows 10+ (suporte a cores ANSI)
- ✅ VS Code Terminal
- ⚠️ Cmd.exe antigo (cores podem não funcionar, use `--no-progress`)

---

## Próximos Passos

Ideias para futuras melhorias:

1. **WebSocket live updates**: Dashboard atualizando em tempo real
2. **Métricas Flink**: Integrar com métricas nativas do Flink
3. **Notificações**: Email/Slack ao final da execução
4. **Histórico**: Comparar execuções anteriores
5. **Grafana**: Integração para monitoramento contínuo

---

## Troubleshooting

### Problema: Cores não aparecem no terminal
**Solução**: Use `--no-progress` ou atualize seu terminal

### Problema: Dashboard não abre
**Solução**: Use o caminho absoluto: `file:///caminho/completo/dashboard.html`

### Problema: Barra de progresso piscando
**Solução**: Normal em terminais lentos, pode ser desabilitado editando `update_progress()`

---

## Referências

- [ANSI Color Codes](https://en.wikipedia.org/wiki/ANSI_escape_code)
- [Chart.js](https://www.chartjs.org/) (para futuras visualizações avançadas)
- [Apache Flink Metrics](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/metrics/)
