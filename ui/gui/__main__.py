import sys
from PyQt5.QtWidgets import QApplication
from ui.ui_manager import MainWindow
from ui.ui_manager import HomeWindow

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', action='store', default='192.168.2.10')
    parser.add_argument('--simulator', action='store_true', default=False)
    ns = parser.parse_known_args()[0]
    
    if ns.simulator:
        ns.device = '127.0.0.1'
        import subprocess
        # Запуск логики ПЛК в отдельном процессе
        logic = subprocess.Popen(["python", "krax.py"])
    
    # Создание и запуск UI
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    window2 = HomeWindow()
    window2.show()
    
    exit_code = app.exec_()
    
    if ns.simulator:
        logic.terminate()
    
    sys.exit(exit_code)

if __name__ == '__main__':
    main()