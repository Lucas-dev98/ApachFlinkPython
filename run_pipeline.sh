#!/usr/bin/env bash
set -euo pipefail

# Script de Automação Completa - PyFlink Big Data Pipeline
# =========================================================
# Este script automatiza todo o processo de setup e execução do pipeline PyFlink
# Agora com interface de progresso e dashboard HTML!

echo "=========================================="
echo "🚀 Automação PyFlink Big Data Pipeline"
echo "=========================================="
echo ""

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_ROOT"

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

step() {
    echo -e "${BLUE}▶ $1${NC}"
}

success() {
    echo -e "${GREEN}✓ $1${NC}"
}

warn() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

info() {
    echo -e "${CYAN}ℹ $1${NC}"
}

# 1. Ativar ambiente Python
step "1. Ativando ambiente Python..."
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv >/dev/null 2>&1; then
    eval "$(pyenv init -)"
    if pyenv versions --bare | grep -qx "3.10.12"; then
        pyenv shell 3.10.12
        success "Python 3.10.12 ativado"
    fi
fi

if [ -f "venv_py310/bin/activate" ]; then
    source venv_py310/bin/activate
    success "Virtualenv ativado"
else
    warn "Virtualenv não encontrado em venv_py310/"
    exit 1
fi

# 2. Verificar/Baixar Flink
step "2. Verificando instalação do Flink..."
if [ ! -d "flink/apache-flink-1.18.1" ]; then
    echo "Flink não encontrado. Executando setup..."
    ./setup.sh
    success "Flink instalado"
else
    success "Flink já instalado"
fi

# 3. Configurar variáveis de ambiente
step "3. Configurando variáveis de ambiente..."
if [ -f "env.sh" ]; then
    source env.sh
    success "Variáveis de ambiente carregadas"
else
    export FLINK_HOME="$PROJECT_ROOT/flink/apache-flink-1.18.1"
    export PATH="$FLINK_HOME/bin:$PATH"
    warn "env.sh não encontrado, usando FLINK_HOME=$FLINK_HOME"
fi

# 4. Iniciar cluster Flink
step "4. Iniciando cluster Flink local..."
if pgrep -f "org.apache.flink" > /dev/null; then
    warn "Cluster Flink já está rodando"
else
    ./start-flink.sh
    sleep 3
    success "Cluster Flink iniciado"
fi

# 5. Verificar WebUI
step "5. Verificando Flink WebUI..."
if curl -s http://localhost:8081 > /dev/null 2>&1; then
    success "WebUI disponível em: http://localhost:8081"
else
    warn "WebUI não está respondendo ainda (pode demorar alguns segundos)"
fi

# 6. Executar pipeline NYC Taxi
step "6. Executando pipeline PyFlink com interface de progresso..."
echo ""
python examples/pyflink_nyc_taxi_csv.py

# 7. Gerar Dashboard HTML
step "7. Gerando Dashboard HTML interativo..."
echo ""
python examples/generate_dashboard.py data/output/nyc_taxi_analysis
DASHBOARD_PATH="$(pwd)/data/output/dashboard.html"

# 8. Mostrar resultados
step "8. Resumo dos Resultados"
echo ""
echo "=========================================="
echo "📊 Análises Geradas:"
echo "=========================================="

if [ -d "data/output/nyc_taxi_analysis" ]; then
    for analysis in top_routes revenue_by_hour trips_by_distance; do
        if [ -d "data/output/nyc_taxi_analysis/$analysis" ]; then
            echo ""
            echo "--- $analysis ---"
            find "data/output/nyc_taxi_analysis/$analysis" -type f \( -name "*.csv" -o -name "part-*" \) | head -1 | xargs head -5 2>/dev/null || echo "Arquivo não encontrado"
        fi
    done
fi

echo ""
echo "=========================================="
echo "✅ Pipeline concluído com sucesso!"
echo "=========================================="
echo ""
info "📊 Dashboard HTML disponível em:"
info "   file://$DASHBOARD_PATH"
echo ""
info "💡 Dica: Abra o dashboard no seu navegador para visualizar os resultados!"
echo ""
echo "📁 Resultados completos em: data/output/nyc_taxi_analysis/"
echo "🌐 Flink WebUI: http://localhost:8081"
echo ""
echo "Para parar o cluster: ./stop-flink.sh"
echo ""
