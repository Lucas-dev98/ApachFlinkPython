#!/bin/bash
# Script para iniciar dashboard em tempo real

cd "$(dirname "$0")"

echo "════════════════════════════════════════════════════════════════"
echo "🌐 Iniciando Dashboard em Tempo Real"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Ativar ambiente
if [ -f "env.sh" ]; then
    source env.sh
fi

if [ -f "venv_py310/bin/activate" ]; then
    source venv_py310/bin/activate
fi

# Iniciar servidor
python3 examples/dashboard_server.py 8000
