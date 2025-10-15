#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# 🚀 COMANDOS PARA EXECUTAR O PROJETO - Apache Flink + PyFlink
# ═══════════════════════════════════════════════════════════════
#
# IMPORTANTE: Execute estes comandos na RAIZ do projeto!
#             cd ~/apacheFlink
#
# ═══════════════════════════════════════════════════════════════

echo "════════════════════════════════════════════════════════════════"
echo "🚀 COMANDOS APACHE FLINK + PYFLINK"
echo "════════════════════════════════════════════════════════════════"
echo ""

# ═══════════════════════════════════════════════════════════════
# OPÇÃO 1: EXECUÇÃO AUTOMATIZADA (MAIS FÁCIL) ⭐
# ═══════════════════════════════════════════════════════════════
echo "1️⃣  EXECUÇÃO AUTOMATIZADA (Recomendado)"
echo ""
echo "   # Navegue até a raiz do projeto"
echo "   cd ~/apacheFlink"
echo ""
echo "   # Execute o script automatizado"
echo "   ./run_pipeline.sh"
echo ""
echo "   ✅ Esse comando faz TUDO automaticamente!"
echo "   - Ativa o ambiente Python"
echo "   - Inicia o cluster Flink"
echo "   - Executa o pipeline"
echo "   - Gera o dashboard"
echo "   - Para o cluster"
echo ""

# ═══════════════════════════════════════════════════════════════
# OPÇÃO 2: EXECUÇÃO MANUAL PASSO A PASSO
# ═══════════════════════════════════════════════════════════════
echo "════════════════════════════════════════════════════════════════"
echo "2️⃣  EXECUÇÃO MANUAL PASSO A PASSO"
echo "════════════════════════════════════════════════════════════════"
echo ""

echo "   Passo 1: Navegue até a raiz do projeto"
echo "   ────────────────────────────────────────"
echo "   cd ~/apacheFlink"
echo ""

echo "   Passo 2: Ative o ambiente"
echo "   ────────────────────────────────────────"
echo "   source env.sh"
echo "   source venv_py310/bin/activate"
echo ""

echo "   Passo 3: Inicie o cluster Flink"
echo "   ────────────────────────────────────────"
echo "   ./start-flink.sh"
echo ""
echo "   # Verificar se está rodando:"
echo "   jps  # Deve mostrar: StandaloneSessionClusterEntrypoint, TaskManagerRunner"
echo ""
echo "   # Acessar WebUI (opcional):"
echo "   xdg-open http://localhost:8081"
echo ""

echo "   Passo 4: Execute o pipeline"
echo "   ────────────────────────────────────────"
echo "   python examples/pyflink_nyc_taxi_csv.py"
echo ""
echo "   # Ou com download automático do dataset:"
echo "   python examples/pyflink_nyc_taxi_csv.py --download"
echo ""
echo "   # Ou sem interface de progresso:"
echo "   python examples/pyflink_nyc_taxi_csv.py --no-progress"
echo ""

echo "   Passo 5: Gere o dashboard HTML"
echo "   ────────────────────────────────────────"
echo "   python examples/generate_dashboard.py data/output/nyc_taxi_analysis"
echo ""
echo "   # Abrir no navegador:"
echo "   xdg-open data/output/dashboard.html"
echo ""

echo "   Passo 6: Pare o cluster"
echo "   ────────────────────────────────────────"
echo "   ./stop-flink.sh"
echo ""

# ═══════════════════════════════════════════════════════════════
# OPÇÃO 3: COMANDOS ÚTEIS INDIVIDUAIS
# ═══════════════════════════════════════════════════════════════
echo "════════════════════════════════════════════════════════════════"
echo "3️⃣  COMANDOS ÚTEIS INDIVIDUAIS"
echo "════════════════════════════════════════════════════════════════"
echo ""

echo "   📥 Baixar dataset automaticamente:"
echo "   ────────────────────────────────────────"
echo "   cd ~/apacheFlink"
echo "   source env.sh && source venv_py310/bin/activate"
echo "   python examples/pyflink_nyc_taxi_csv.py --download"
echo ""

echo "   📊 Ver resultados no terminal:"
echo "   ────────────────────────────────────────"
echo "   cd ~/apacheFlink"
echo "   head -20 data/output/nyc_taxi_analysis/top_routes/part-*"
echo "   head -30 data/output/nyc_taxi_analysis/revenue_by_hour/part-*"
echo "   head -10 data/output/nyc_taxi_analysis/trips_by_distance/part-*"
echo ""

echo "   🧹 Limpar resultados anteriores:"
echo "   ────────────────────────────────────────"
echo "   cd ~/apacheFlink"
echo "   rm -rf data/output/nyc_taxi_analysis/*"
echo "   rm -f data/output/dashboard.html"
echo ""

echo "   🔍 Ver logs do Flink:"
echo "   ────────────────────────────────────────"
echo "   cd ~/apacheFlink"
echo "   tail -f flink/apache-flink-1.18.1/log/flink-*-standalonesession-*.log"
echo ""

echo "   🌐 Abrir Flink WebUI:"
echo "   ────────────────────────────────────────"
echo "   xdg-open http://localhost:8081"
echo ""

echo "   🛑 Parar cluster Flink (se travado):"
echo "   ────────────────────────────────────────"
echo "   cd ~/apacheFlink"
echo "   ./stop-flink.sh"
echo "   pkill -f flink  # Se necessário"
echo ""

# ═══════════════════════════════════════════════════════════════
# TROUBLESHOOTING
# ═══════════════════════════════════════════════════════════════
echo "════════════════════════════════════════════════════════════════"
echo "🛠️  TROUBLESHOOTING"
echo "════════════════════════════════════════════════════════════════"
echo ""

echo "   ❌ Erro: 'env.sh: Arquivo ou diretório inexistente'"
echo "   ────────────────────────────────────────"
echo "   Solução: Você está no diretório errado!"
echo "   cd ~/apacheFlink  # Volte para a raiz do projeto"
echo ""

echo "   ❌ Erro: 'python: command not found'"
echo "   ────────────────────────────────────────"
echo "   Solução: Ative o virtualenv primeiro"
echo "   source venv_py310/bin/activate"
echo ""

echo "   ❌ Erro: './start-flink.sh: Arquivo não encontrado'"
echo "   ────────────────────────────────────────"
echo "   Solução: Navegue até a raiz do projeto"
echo "   cd ~/apacheFlink"
echo ""

echo "   ❌ Erro: 'Permission denied'"
echo "   ────────────────────────────────────────"
echo "   Solução: Dê permissão de execução"
echo "   chmod +x *.sh"
echo ""

echo "   ❌ Erro: 'Address already in use (8081)'"
echo "   ────────────────────────────────────────"
echo "   Solução: Pare o cluster e reinicie"
echo "   ./stop-flink.sh"
echo "   pkill -f flink"
echo "   ./start-flink.sh"
echo ""

# ═══════════════════════════════════════════════════════════════
# COMANDO COMPLETO COPY-PASTE
# ═══════════════════════════════════════════════════════════════
echo "════════════════════════════════════════════════════════════════"
echo "📋 COMANDO COMPLETO (COPY & PASTE)"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "# Copie e cole isto no terminal (executa tudo de uma vez):"
echo ""
echo "cd ~/apacheFlink && \\"
echo "source env.sh && \\"
echo "source venv_py310/bin/activate && \\"
echo "./start-flink.sh && \\"
echo "sleep 5 && \\"
echo "python examples/pyflink_nyc_taxi_csv.py && \\"
echo "python examples/generate_dashboard.py data/output/nyc_taxi_analysis && \\"
echo "xdg-open data/output/dashboard.html && \\"
echo "./stop-flink.sh"
echo ""

# ═══════════════════════════════════════════════════════════════
# LINKS IMPORTANTES
# ═══════════════════════════════════════════════════════════════
echo "════════════════════════════════════════════════════════════════"
echo "🔗 LINKS IMPORTANTES"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "  📂 Diretório do Projeto: ~/apacheFlink"
echo "  🌐 GitHub:               https://github.com/Lucas-dev98/ApachFlinkPython"
echo "  🖥️  Flink WebUI:          http://localhost:8081"
echo "  📊 Dashboard HTML:       file://$(cd ~/apacheFlink 2>/dev/null && pwd)/data/output/dashboard.html"
echo ""

echo "════════════════════════════════════════════════════════════════"
echo "✅ Para ver este guia novamente, execute:"
echo "   cat ~/apacheFlink/QUICK_START.sh"
echo "════════════════════════════════════════════════════════════════"
