# Импорт необходимых модулей
from pyplc.pou import POU                     # Базовый класс для программ логики
from pyplc.platform import plc, hw, board     # Основные объекты для работы с контроллером
from sys import platform                      # Для определения операционной системы
from pyplc.utils.latch import RS              # Триггер с приоритетом Reset

# 1. Управление ленточным питателем с помощью RS-триггера
belt_feeder = RS(
    set=lambda: hw.DI_PANEL1_START,                  # Условие включения - кнопка START
    reset=lambda: hw.DI_BELTFEEDER_ROPESWITCH_TRIPPED, # Условие выключения - аварийный выключатель
    q=hw.DO_BELTFEEDER_TURNON                        # Выход на включение питателя
)

# 2. Функция управления горелкой
def control_burner():
    # Проверяем, что горелка не в резервном режиме
    if not hw.DI_BURNER_CONTROL_RESERVE:
        target_temp = 60.0  # Целевая температура 60°C
        current_temp = hw.AI_TEMP_TUMBLEDRYER_ENTER  # Текущая температура
        
        # Если температура ниже целевой
        if current_temp < target_temp:
            # Простой П-регулятор: мощность = (разница температур) * коэффициент
            power = (target_temp - current_temp) * 2
            # Ограничиваем мощность диапазоном 0-100%
            hw.AO_TEMP_BURNER_TASK = min(max(power, 0), 100)
        else:
            # Если температура достигнута - выключаем горелку
            hw.AO_TEMP_BURNER_TASK = 0

# 3. Функция аварийной остановки
def emergency_stop():
    # Проверяем условия аварийной остановки:
    # - кнопка STOP на панели
    # - срабатывание датчика обрыва ленты
    if hw.DI_PANEL1_STOP or hw.DI_BELTFEEDER_BELTBREAK_TRIPPED:
        # Отключаем все дискретные выходы (DO_*)
        for attr in dir(hw):
            if attr.startswith('DO_'):
                setattr(hw, attr, False)
        # Выключаем горелку (устанавливаем мощность в 0)
        hw.AO_TEMP_BURNER_TASK = 0

# Основная программа (может быть пустой, так как логика в отдельных функциях)
def plc_prg():
    while True:
        yield  # Пауза между циклами выполнения

# Формируем список программ для выполнения
instances = [belt_feeder, control_burner, emergency_stop]

# Если работаем на Linux, можно добавить дополнительные программы
if platform == "linux":
    # Здесь можно добавить специфичные для Linux программы
    pass

# Запускаем основной цикл выполнения программ
plc.run(instances=instances, ctx=globals())