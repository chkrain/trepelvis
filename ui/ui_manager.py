from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from krax import controllers, set_input, get_output

class MainWindow(QMainWindow):
    STATION_MAPPING = {
        'STATION1': 'beltfeeder',
        'STATION2': 'rotarycrusher',
        'STATION3': 'convcrusher',
        'STATION4': 'rollercrusher',
        'STATION5': 'convbolt',
        'STATION6': 'doublemeshscreen',
        'STATION7': 'convhopper',
        'STATION8': 'hopper',
        'STATION9': 'convpacking',
        'STATION10': 'burner',
        'STATION11': 'drum',
        'STATION12': 'fan',
        'STATION13': 'auger',
        'STATION14': 'filter',
        'STATION15': 'convdrum',
        'STATION16': 'rollercrusher_2',
        'STATION17': 'convscreen_2',
        'STATION18': 'doublemeshscreen_2',
        'STATION19': 'conv_bin_38',
        'STATION20': 'hopper_bin_38',
        'STATION21': 'convpacking_bin_02',
        'STATION22': 'convhopper_bin_02',
        'STATION23': 'hopper_bin_02'
    }

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setup_ui_connections()
        self.setup_status_timer()

    def setup_ui_connections(self):
        """Настройка соединений сигналов и слотов"""
        for station_id, prefix in self.STATION_MAPPING.items():
            # Кнопки ручного режима
            btn_manual = getattr(self, f"manual_{prefix}", None)
            if btn_manual:
                btn_manual.clicked.connect(lambda _, s=station_id: set_input(s, 'MANUAL', True))
                btn_manual.released.connect(
                    lambda _, s=station_id: set_input(s, 'MANUAL', False))
            
            # Кнопки ПУСК
            btn_start = getattr(self, f"start_{prefix}", None)
            if btn_start:
                btn_start.clicked.connect(
                    lambda _, s=station_id: set_input(s, 'START', True))
                btn_start.released.connect(
                    lambda _, s=station_id: set_input(s, 'START', False))
            
            # Кнопки СТОП
            btn_stop = getattr(self, f"stop_{prefix}", None)
            if btn_stop:
                btn_stop.clicked.connect(
                    lambda _, s=station_id: set_input(s, 'STOP', True))
                btn_stop.released.connect(
                    lambda _, s=station_id: set_input(s, 'STOP', False))

    def setup_status_timer(self):
        """Таймер для обновления статуса станций"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_station_status)
        self.timer.start(100)  # Обновление каждые 100 мс

    def update_station_status(self):
        """Обновление визуального статуса станций"""
        for station_id, prefix in self.STATION_MAPPING.items():
            status_label = getattr(self, f"label_{prefix}", None)
            if not status_label:
                continue
            
            # Получаем состояние выхода (активность)
            is_active = get_output(station_id)
            
            # Обновляем цвет в зависимости от состояния
            if is_active:
                status_label.setStyleSheet("background: green; color: white;")
            else:
                status_label.setStyleSheet("background: gray; color: white;")