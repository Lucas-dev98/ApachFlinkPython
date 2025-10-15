#!/usr/bin/env python3
"""
Servidor HTTP para Dashboard em Tempo Real
==========================================
Serve o dashboard e fornece API para dados em tempo real
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import threading
import time
from pathlib import Path
import glob


class DashboardHandler(SimpleHTTPRequestHandler):
    """Handler customizado para servir dashboard e API"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/' or self.path == '/index.html':
            # Servir dashboard_live.html
            dashboard_path = os.path.join(os.path.dirname(__file__), 'dashboard_live.html')
            try:
                with open(dashboard_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(content)
                return
            except FileNotFoundError:
                self.send_error(404, f"Dashboard not found at {dashboard_path}")
                return
        elif self.path == '/api/status':
            self.send_json_response(self.get_pipeline_status())
        elif self.path == '/api/results':
            self.send_json_response(self.get_results_data())
        else:
            return SimpleHTTPRequestHandler.do_GET(self)
    
    def send_json_response(self, data):
        """Envia resposta JSON"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def get_pipeline_status(self):
        """Obtém status atual do pipeline"""
        report_path = 'data/output/nyc_taxi_analysis/execution_report.json'
        
        if os.path.exists(report_path):
            with open(report_path, 'r') as f:
                return json.load(f)
        
        return {
            'status': 'waiting',
            'message': 'Aguardando execução do pipeline...'
        }
    
    def get_results_data(self):
        """Obtém dados dos resultados"""
        results = {
            'top_routes': [],
            'revenue_by_hour': [],
            'trips_by_distance': []
        }
        
        base_path = 'data/output/nyc_taxi_analysis'
        
        # Top Routes
        routes_files = glob.glob(f'{base_path}/top_routes/part-*')
        if routes_files:
            results['top_routes'] = self.read_csv_data(routes_files[0])
        
        # Revenue by Hour
        revenue_files = glob.glob(f'{base_path}/revenue_by_hour/part-*')
        if revenue_files:
            results['revenue_by_hour'] = self.read_csv_data(revenue_files[0])
        
        # Trips by Distance
        distance_files = glob.glob(f'{base_path}/trips_by_distance/part-*')
        if distance_files:
            results['trips_by_distance'] = self.read_csv_data(distance_files[0])
        
        return results
    
    def read_csv_data(self, file_path):
        """Lê dados de arquivo CSV"""
        import csv
        data = []
        try:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                data = list(reader)
        except Exception as e:
            print(f"Erro ao ler {file_path}: {e}")
        return data


def start_server(port=8000):
    """Inicia servidor HTTP"""
    os.chdir('/home/lucasbastos/apacheFlink')
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, DashboardHandler)
    
    print(f"""
════════════════════════════════════════════════════════════════
🌐 DASHBOARD EM TEMPO REAL INICIADO
════════════════════════════════════════════════════════════════

  📊 Dashboard URL:  http://localhost:{port}
  🔌 API Status:     http://localhost:{port}/api/status
  📈 API Results:    http://localhost:{port}/api/results

════════════════════════════════════════════════════════════════

Execute o pipeline em outro terminal:
  cd ~/apacheFlink
  ./run_pipeline.sh

O dashboard será atualizado automaticamente!

Pressione Ctrl+C para parar o servidor.
════════════════════════════════════════════════════════════════
    """)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Servidor encerrado.")
        httpd.server_close()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    start_server(port)
