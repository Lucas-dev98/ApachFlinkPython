#!/bin/bash
# COMANDOS PRINCIPAIS - Apache Flink + PyFlink

echo "=========================================="
echo "🚀 APACHE FLINK + PYFLINK"
echo "=========================================="
echo

# 1. SETUP INICIAL
echo "1️⃣  CONFIGURAÇÃO INICIAL"
echo "   ./setup.sh"
echo "   source env.sh"
echo "   source venv_py310/bin/activate"
echo

# 2. GERENCIAR CLUSTER
echo "2️⃣  GERENCIAR CLUSTER"
echo "   ./start-flink.sh              # Iniciar"
echo "   ./stop-flink.sh               # Parar"
echo "   http://localhost:8081         # WebUI"
echo

# 3. EXECUTAR PIPELINES
echo "3️⃣  EXECUTAR PIPELINES"
echo "   # Pipeline NYC Taxi (Big Data)"
echo "   python examples/pyflink_nyc_taxi_csv.py --download"
echo
echo "   # Exemplo simples Top-N"
echo "   python examples/pyflink_topn.py"
echo

# 4. VER RESULTADOS
echo "4️⃣  VER RESULTADOS"
echo "   cat data/output/nyc_taxi_analysis/top_routes/*"
echo "   cat data/output/nyc_taxi_analysis/revenue_by_hour/*"
echo "   cat data/output/nyc_taxi_analysis/trips_by_distance/*"
echo

# 5. LOGS E DEBUG
echo "5️⃣  LOGS E DEBUG"
echo "   tail -f flink/apache-flink-1.18.1/log/*.log"
echo "   cat pipeline_csv.log"
echo

# 6. LIMPEZA
echo "6️⃣  LIMPEZA"
echo "   rm -rf data/output/nyc_taxi_analysis/*"
echo "   rm -f pipeline_csv.log"
echo

echo "=========================================="
echo "📚 DOCUMENTAÇÃO"
echo "=========================================="
echo "README.md           - Documentação completa"
echo "RESUMO_FINAL.txt    - Resumo do projeto"
echo "=========================================="
