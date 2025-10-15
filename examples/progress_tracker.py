"""
Interface de Acompanhamento de Execução - Apache Flink Pipeline
================================================================
Módulo para tracking visual de progresso, logging colorido e estatísticas
"""

import sys
import time
from datetime import datetime
from typing import Optional, Dict, Any
import json


class Colors:
    """Códigos ANSI para cores no terminal"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Cores principais
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'


class ProgressTracker:
    """
    Classe para tracking de progresso da pipeline com interface visual
    """
    
    def __init__(self, total_steps: int = 100, show_timestamps: bool = True):
        self.total_steps = total_steps
        self.current_step = 0
        self.show_timestamps = show_timestamps
        self.start_time = None
        self.step_times = []
        self.current_phase = None
        self.stats = {
            'records_processed': 0,
            'analyses_completed': 0,
            'errors': 0,
            'warnings': 0
        }
        
    def start(self, title: str = "Pipeline de Processamento"):
        """Inicia o tracking de progresso"""
        self.start_time = time.time()
        self._print_header(title)
        
    def _print_header(self, title: str):
        """Imprime cabeçalho visual"""
        width = 80
        print(f"\n{Colors.CYAN}{'=' * width}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{title.center(width)}{Colors.RESET}")
        print(f"{Colors.CYAN}{'=' * width}{Colors.RESET}\n")
        
    def start_phase(self, phase_name: str, description: str = ""):
        """Inicia uma nova fase do processamento"""
        self.current_phase = phase_name
        timestamp = self._get_timestamp()
        
        print(f"\n{Colors.BOLD}{Colors.BLUE}▶ {phase_name}{Colors.RESET}")
        if description:
            print(f"  {Colors.WHITE}{description}{Colors.RESET}")
        if self.show_timestamps:
            print(f"  {Colors.CYAN}[{timestamp}]{Colors.RESET}")
            
    def update_progress(self, step: int, message: str = ""):
        """Atualiza a barra de progresso"""
        self.current_step = step
        percentage = (step / self.total_steps) * 100
        bar_length = 50
        filled_length = int(bar_length * step // self.total_steps)
        
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        # Calcula tempo estimado
        if self.start_time and step > 0:
            elapsed = time.time() - self.start_time
            eta = (elapsed / step) * (self.total_steps - step)
            eta_str = self._format_time(eta)
        else:
            eta_str = "calculando..."
            
        sys.stdout.write(f'\r  {Colors.GREEN}[{bar}]{Colors.RESET} {percentage:.1f}% | ETA: {eta_str}')
        if message:
            sys.stdout.write(f' | {message}')
        sys.stdout.flush()
        
    def log_info(self, message: str):
        """Log de informação"""
        timestamp = self._get_timestamp()
        prefix = f"[{timestamp}]" if self.show_timestamps else ""
        print(f"\n  {Colors.CYAN}ℹ{Colors.RESET} {prefix} {message}")
        
    def log_success(self, message: str):
        """Log de sucesso"""
        timestamp = self._get_timestamp()
        prefix = f"[{timestamp}]" if self.show_timestamps else ""
        print(f"\n  {Colors.GREEN}✓{Colors.RESET} {prefix} {Colors.GREEN}{message}{Colors.RESET}")
        
    def log_warning(self, message: str):
        """Log de aviso"""
        timestamp = self._get_timestamp()
        prefix = f"[{timestamp}]" if self.show_timestamps else ""
        print(f"\n  {Colors.YELLOW}⚠{Colors.RESET} {prefix} {Colors.YELLOW}{message}{Colors.RESET}")
        self.stats['warnings'] += 1
        
    def log_error(self, message: str):
        """Log de erro"""
        timestamp = self._get_timestamp()
        prefix = f"[{timestamp}]" if self.show_timestamps else ""
        print(f"\n  {Colors.RED}✗{Colors.RESET} {prefix} {Colors.RED}{message}{Colors.RESET}")
        self.stats['errors'] += 1
        
    def complete_phase(self, records_count: Optional[int] = None):
        """Completa a fase atual"""
        if records_count:
            self.stats['records_processed'] += records_count
            self.log_success(f"Fase '{self.current_phase}' concluída - {records_count:,} registros processados")
        else:
            self.log_success(f"Fase '{self.current_phase}' concluída")
            
    def complete_analysis(self, analysis_name: str, output_path: str, row_count: int):
        """Registra conclusão de uma análise"""
        self.stats['analyses_completed'] += 1
        self.log_success(f"Análise '{analysis_name}' finalizada")
        print(f"    📊 Resultados: {row_count} linhas")
        print(f"    📁 Arquivo: {output_path}")
        
    def update_stats(self, **kwargs):
        """Atualiza estatísticas customizadas"""
        self.stats.update(kwargs)
        
    def print_stats(self):
        """Imprime estatísticas finais"""
        elapsed = time.time() - self.start_time if self.start_time else 0
        elapsed_str = self._format_time(elapsed)
        
        print(f"\n\n{Colors.CYAN}{'─' * 80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}📊 ESTATÍSTICAS FINAIS{Colors.RESET}")
        print(f"{Colors.CYAN}{'─' * 80}{Colors.RESET}\n")
        
        # Estatísticas principais
        stats_display = [
            ("⏱️  Tempo Total", elapsed_str),
            ("📝 Registros Processados", f"{self.stats['records_processed']:,}"),
            ("✅ Análises Concluídas", str(self.stats['analyses_completed'])),
            ("⚠️  Avisos", str(self.stats['warnings'])),
            ("❌ Erros", str(self.stats['errors']))
        ]
        
        for label, value in stats_display:
            print(f"  {Colors.WHITE}{label:.<40}{Colors.RESET} {Colors.GREEN}{value:>20}{Colors.RESET}")
            
        # Throughput
        if elapsed > 0 and self.stats['records_processed'] > 0:
            throughput = self.stats['records_processed'] / elapsed
            print(f"  {Colors.WHITE}{'⚡ Throughput':.<40}{Colors.RESET} {Colors.GREEN}{throughput:>17,.1f} rec/s{Colors.RESET}")
            
        print(f"\n{Colors.CYAN}{'─' * 80}{Colors.RESET}\n")
        
    def _get_timestamp(self) -> str:
        """Retorna timestamp formatado"""
        return datetime.now().strftime("%H:%M:%S")
        
    def _format_time(self, seconds: float) -> str:
        """Formata tempo em formato legível"""
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = int(seconds // 60)
            secs = int(seconds % 60)
            return f"{minutes}m {secs}s"
        else:
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            return f"{hours}h {minutes}m"
            
    def finish(self, success: bool = True):
        """Finaliza o tracking"""
        if success:
            print(f"\n\n{Colors.BG_GREEN}{Colors.BOLD} ✓ PIPELINE CONCLUÍDA COM SUCESSO {Colors.RESET}")
        else:
            print(f"\n\n{Colors.BG_RED}{Colors.BOLD} ✗ PIPELINE FINALIZADA COM ERROS {Colors.RESET}")
            
        self.print_stats()
        
    def save_report(self, output_path: str):
        """Salva relatório em JSON"""
        elapsed = time.time() - self.start_time if self.start_time else 0
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'execution_time_seconds': elapsed,
            'statistics': self.stats,
            'success': self.stats['errors'] == 0
        }
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
            
        self.log_info(f"Relatório salvo em: {output_path}")


class SimpleProgressBar:
    """Barra de progresso simples para loops"""
    
    def __init__(self, total: int, prefix: str = "Progresso", length: int = 40):
        self.total = total
        self.prefix = prefix
        self.length = length
        self.current = 0
        
    def update(self, increment: int = 1):
        """Atualiza a barra"""
        self.current += increment
        percentage = (self.current / self.total) * 100
        filled = int(self.length * self.current // self.total)
        bar = '█' * filled + '░' * (self.length - filled)
        
        sys.stdout.write(f'\r{self.prefix}: [{bar}] {percentage:.1f}% ({self.current}/{self.total})')
        sys.stdout.flush()
        
        if self.current >= self.total:
            print()  # Nova linha ao completar


# Exemplo de uso
if __name__ == "__main__":
    # Teste básico do ProgressTracker
    tracker = ProgressTracker(total_steps=100)
    tracker.start("Teste de Pipeline")
    
    tracker.start_phase("Download de Dados", "Baixando dataset de exemplo...")
    time.sleep(1)
    tracker.complete_phase(10000)
    
    tracker.start_phase("Processamento", "Aplicando transformações...")
    for i in range(1, 101):
        tracker.update_progress(i, f"Processando batch {i}/100")
        time.sleep(0.05)
    print()
    tracker.complete_phase(50000)
    
    tracker.start_phase("Análises", "Executando análises SQL...")
    tracker.complete_analysis("Top Routes", "/tmp/output/top_routes.csv", 10)
    tracker.complete_analysis("Revenue by Hour", "/tmp/output/revenue.csv", 24)
    
    tracker.log_warning("Alguns registros com dados incompletos foram ignorados")
    
    tracker.finish(success=True)
