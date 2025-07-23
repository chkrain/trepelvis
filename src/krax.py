from pyplc.platform import plc
from pyplc.pou import POU
from pyplc.utils.latch import RS
from pyplc.sfc import SFC

class EquipmentControl(SFC):
    """Основной класс управления оборудованием с защитами"""

    # Аналоговые входы
    temp_tumble_dryer_enter = POU.input(0.0)      # AI_TEMP_TUMBLEDRYER_ENTER
    temp_tumble_dryer_exit = POU.input(0.0)       # AI_TEMP_TUMBLEDRYER_EXIT
    humidity_tumble_dryer_exit = POU.input(0.0)   # AI_HUMIDITY_TUMBLEDRYER_EXIT
    ai_reserve = POU.input(0.0)                   # AI_RESERVE

    # Аналоговые выходы
    temp_burner_task = POU.output(0.0)            # AO_TEMP_BURNER_TASK
    ao_reserve = POU.output(0.0)                  # AO_RESERVE

    # Дискретные выходы
    # Модуль 3
    belt_feeder_on = POU.output(False)            # DO_BELTFEEDER_TURNON
    rotary_crusher_on = POU.output(False)         # DO_ROTARYCRUSHER_TURNON
    conveyor6506000_crusher_on = POU.output(False) # DO_CONVEYOR6506000_CRUSHER_TURNON
    roller_crusher_on = POU.output(False)         # DO_ROLLERCRUSHER_TURNON
    conveyor6506000_bolt_on = POU.output(False)   # DO_CONVEYOR6506000_BOLT_TURNON
    double_mesh_screen_on = POU.output(False)     # DO_DOUBLEMESHCSREEN_TURNON
    conveyor6506000_hopper_on = POU.output(False) # DO_CONVEYOR6506000_HOPPER_TURNON
    hopper_gate_open_reserve = POU.output(False)  # DO_HOPPERGATE_OPEN_RESERVE

    # Модуль 4
    hopper_gate_close_reserve = POU.output(False) # DO_HOPPERGATE_CLOSE_RESERVE
    conveyor6506000_packing_on = POU.output(False) # DO_CONVEYOR6506000_PACKING_TURNON
    conveyor6501000_drum_on = POU.output(False)   # DO_CONVEYOR6501000_DRUM_TURNON
    burner_start_allow = POU.output(False)        # DO_BURNER_STARTALLOW
    burner_control_reserve = POU.output(False)    # DO_BURNER_CONTROL_RESERVE
    burner_control2_reserve = POU.output(False)   # DO_BURNER_CONTROL2_RESERVE
    drum_on = POU.output(False)                   # DO_DRUM_TURNON
    fan_on = POU.output(False)                    # DO_FAN_TURNON

    # Модуль 5
    sludge_auger_on = POU.output(False)           # DO_SLUDGEAUGER_TURNON
    filter_start_allow = POU.output(False)        # DO_FILTER_STARTALLOW
    filter_control_reserve = POU.output(False)    # DO_FILTER_CONTROL_RESERVE
    conveyor6508000_drum_on = POU.output(False)   # DO_CONVEYOR6508000_DRUM_TURNON
    roller_crusher2_on = POU.output(False)        # DO_ROLLERCRUSHER2_TURNON
    conveyor6508000_screen_on = POU.output(False) # DO_CONVEYOR6508000_SCREEN_TURNON
    double_mesh_screen2_on = POU.output(False)    # DO_DOUBLEMESHSCREEN2_TURNON
    conveyor6506000_bin38_on = POU.output(False)  # DO_CONVEYOR6506000_BIN38_TURNON

    # Модуль 6
    bin38_vibrator_on = POU.output(False)         # DO_BIN38VIBRATOR_TURNON
    bin38_gate_open_reserve = POU.output(False)   # DO_BIN38GATE_OPEN_RESERVE
    bin38_gate_close_reserve = POU.output(False)  # DO_BIN38GATE_CLOSE_RESERVE
    conveyor6501000_packing2_on = POU.output(False) # DO_CONVEYOR6501000_PACKING_TURNON
    conveyor6506000_bin02_on = POU.output(False)  # DO_CONVEYOR6506000_BIN02_TURNON
    bin02_vibrator_on = POU.output(False)        # DO_BIN02VIBRATOR_TURNON
    bin02_gate_open_reserve = POU.output(False)  # DO_BIN02GATE_OPEN_RESERVE
    bin02_gate_close_reserve = POU.output(False) # DO_BIN02GATE_CLOSE_RESERVE

    # Модуль 7
    flow_auger_on = POU.output(False)            # DO_FLOWAUGER_TURNON
    horizontal_auger_on = POU.output(False)      # DO_HORIZONTALAUGER_TURNON
    vertical_auger_on = POU.output(False)        # DO_VERTICALAUGER_TURNON
    vent_filter_control_reserve = POU.output(False) # DO_VENTFILTER_CONTROL_RESERVE
    vent_filter_control2_reserve = POU.output(False) # DO_VENTFILTER_CONTROL2_RESERVE
    vent_sludge_auger_on = POU.output(False)     # DO_VENTSLUDGEAUGER_TURNON
    vent_fan_on = POU.output(False)              # DO_VENTFAN_TURNON
    do_reserve_1 = POU.output(False)             # DO_RESERVE_1

    # Модуль 8
    do_reserve_2 = POU.output(False)             # DO_RESERVE_2
    do_reserve_3 = POU.output(False)             # DO_RESERVE_3
    do_reserve_4 = POU.output(False)             # DO_RESERVE_4
    do_reserve_5 = POU.output(False)             # DO_RESERVE_5
    do_reserve_6 = POU.output(False)             # DO_RESERVE_6
    do_reserve_7 = POU.output(False)             # DO_RESERVE_7
    do_reserve_8 = POU.output(False)             # DO_RESERVE_8
    do_reserve_9 = POU.output(False)             # DO_RESERVE_9

    # Модуль 9
    do_reserve_10 = POU.output(False)            # DO_RESERVE_10
    do_reserve_11 = POU.output(False)            # DO_RESERVE_11
    do_reserve_12 = POU.output(False)            # DO_RESERVE_12
    do_reserve_13 = POU.output(False)            # DO_RESERVE_13
    do_reserve_14 = POU.output(False)            # DO_RESERVE_14
    do_reserve_15 = POU.output(False)            # DO_RESERVE_15
    do_reserve_16 = POU.output(False)            # DO_RESERVE_16
    do_reserve_17 = POU.output(False)            # DO_RESERVE_17

    # Дискретные входы
    # Модуль 10
    belt_feeder_rope_switch = POU.input(False)   # DI_BELTFEEDER_ROPESWITCH_TRIPPED
    belt_feeder_belt_break = POU.input(False)    # DI_BELTFEEDER_BELTBREAK_TRIPPED
    rotary_crusher_running = POU.input(False)    # DI_ROTARYCRUSHER_RUNNING
    conveyor6508000_rope_switch = POU.input(False) # DI_CONVEYOR6508000_ROPESWITCH_TRIPPED
    conveyor6508000_belt_break = POU.input(False) # DI_CONVEYOR6508000_BELTBREAK_TRIPPED
    roller_crusher_running = POU.input(False)    # DI_ROLLERCRUSHER_RUNNING
    conveyor6506000_rope_switch = POU.input(False) # DI_CONVEYOR6506000_ROPESWITCH_TRIPPED
    conveyor6506000_belt_break = POU.input(False) # DI_CONVEYOR6506000_BELTBREAK_TRIPPED

    # Модуль 11
    double_mesh_screen_running = POU.input(False) # DI_DOUBLEMESHSCREEN_RUNNING
    conveyor6506000_rope_switch2 = POU.input(False) # DI_CONVEYOR6506000_ROPESWITCH2_TRIPPED
    conveyor6506000_belt_break2 = POU.input(False) # DI_CONVEYOR6506000_BELTBREAK2_TRIPPED
    hopper_high_level = POU.input(False)         # DI_HOPPER_HIGHLEVEL
    hopper_low_level = POU.input(False)          # DI_HOPPER_LOWLEVEL
    hopper_gate_running_reserve = POU.input(False) # DI_HOPPERGATE_RUNNING_RESERVE
    hopper_gate_open_reserve_di = POU.input(False) # DI_HOPPERGATE_OPEN_RESERVE
    hopper_gate_closed_reserve = POU.input(False) # DI_HOPPERGATE_CLOSED_RESERVE

    # Модуль 12
    conveyor6506000_rope_switch3 = POU.input(False) # DI_CONVEYOR6506000_ROPESWITCH3_TRIPPED
    conveyor6506000_belt_break3 = POU.input(False) # DI_CONVEYOR6506000_BELTBREAK3_TRIPPED
    packing_hopper_gate_open = POU.input(False)   # DI_PACKINGHOPPERGATE_OPEN
    conveyor65010000_rope_switch = POU.input(False) # DI_CONVEYOR65010000_ROPESWITCH_TRIPPED
    conveyor65010000_belt_break = POU.input(False) # DI_CONVEYOR65010000_BELTBREAK_TRIPPED
    burner_control_reserve_di = POU.input(False)  # DI_BURNER_CONTROL_RESERVE
    burner_control2_reserve_di = POU.input(False) # DI_BURNER_CONTROL2_RESERVE
    burner_control3_reserve_di = POU.input(False) # DI_BURNER_CONTROL3_RESERVE

    # Модуль 13
    drum_running = POU.input(False)              # DI_DRUM_RUNNING
    auger_running = POU.input(False)             # DI_AUGER_RUNNING
    auger_motion = POU.input(False)              # DI_AUGER_MOTION
    fan_filter_control_reserve = POU.input(False) # DI_FANFILTER_CONTROL_RESERVE
    fan_filter_control2_reserve = POU.input(False) # DI_FANFILTER_CONTROL2_RESERVE
    conveyor6508000_rope_switch2 = POU.input(False) # DI_CONVEYOR6508000_ROPESWITCH2_TRIPPED
    conveyor6508000_belt_break2 = POU.input(False) # DI_CONVEYOR6508000_BELTBREAK2_TRIPPED
    roller_crusher2_running = POU.input(False)   # DI_ROLLERCRUSHER2_RUNNING

    # Модуль 14
    conveyor6508000_rope_switch3 = POU.input(False) # DI_CONVEYOR6508000_ROPESWITCH3_TRIPPED
    conveyor6508000_belt_break3 = POU.input(False) # DI_CONVEYOR6508000_BELTBREAK3_TRIPPED
    double_mesh_screen2_running = POU.input(False) # DI_DOUBLEMESHSCREEN2_RUNNING
    conveyor6506000_rope_switch4 = POU.input(False) # DI_CONVEYOR6506000_ROPESWITCH4_TRIPPED
    conveyor6506000_belt_break4 = POU.input(False) # DI_CONVEYOR6506000_BELTBREAK4_TRIPPED
    bin38_high_level = POU.input(False)          # DI_BIN38_HIGHLEVEL
    bin38_low_level = POU.input(False)           # DI_BIN38_LOWLEVEL
    bin38_gate_running_reserve = POU.input(False) # DI_BIN38GATE_RUNNING_RESERVE

    # Модуль 15
    bin38_gate_open_reserve_di = POU.input(False) # DI_BIN38GATE_OPEN_RESERVE
    bin38_gate_closed_reserve = POU.input(False) # DI_BIN38GATE_CLOSED_RESERVE
    conveyor65010000_rope_switch2 = POU.input(False) # DI_CONVEYOR65010000_ROPESWITCH2_TRIPPED
    conveyor65010000_belt_break2 = POU.input(False) # DI_CONVEYOR65010000_BELTBREAK2_TRIPPED
    packing_hopper_gate2_open = POU.input(False) # DI_PACKINGHOPPERGATE2_OPEN
    conveyor6506000_rope_switch5 = POU.input(False) # DI_CONVEYOR6506000_ROPESWITCH5_TRIPPED
    conveyor6506000_belt_break5 = POU.input(False) # DI_CONVEYOR6506000_BELTBREAK5_TRIPPED
    bin02_high_level = POU.input(False)          # DI_BIN02_HIGHLEVEL

    # Модуль 16
    bin02_low_level = POU.input(False)           # DI_BIN02_LOWLEVEL
    bin02_gate_running_reserve = POU.input(False) # DI_BIN02GATE_RUNNING_RESERVE
    bin02_gate_open_reserve = POU.input(False)   # DI_BIN02GATE_OPEN_RESERVE
    bin02_gate_closed_reserve = POU.input(False) # DI_BIN02GATE_CLOSED_RESERVE
    flow_auger_motion = POU.input(False)         # DI_FLOWAUGER_MOTION
    packing_hopper_high_level = POU.input(False) # DI_PACKINGHOPPER_HIGHLEVEL
    horizontal_auger_motion = POU.input(False)   # DI_HORIZONTALAUGER_MOTION
    horizontal_auger_running = POU.input(False)  # DI_HORIZONTALAUGER_RUNNING

    # Модуль 17
    vertical_auger_motion = POU.input(False)     # DI_VERTICALAUGER_MOTION
    silo02_high_level = POU.input(False)         # DI_SILO02_HIGHLEVEL
    silo02_low_level = POU.input(False)          # DI_SILO02_LOWLEVEL
    vent_auger_motion = POU.input(False)         # DI_VENTAUGER_MOTION
    vent_fan_running = POU.input(False)          # DI_VENTFAN_RUNNING
    di_reserve_1 = POU.input(False)              # DI_RESERVE_1
    di_reserve_2 = POU.input(False)              # DI_RESERVE_2
    di_reserve_3 = POU.input(False)              # DI_RESERVE_3

    # Модуль 18
    di_reserve_4 = POU.input(False)              # DI_RESERVE_4
    panel1_start = POU.input(False)              # DI_PANEL1_START
    panel1_stop = POU.input(False)               # DI_PANEL1_STOP
    panel2_start = POU.input(False)              # DI_PANEL2_START
    panel2_stop = POU.input(False)               # DI_PANEL2_STOP
    station1_manual = POU.input(False)           # DI_STATION1_MANUAL
    station1_start = POU.input(False)            # DI_STATION1_START
    station1_stop = POU.input(False)             # DI_STATION1_STOP

    # Модуль 19
    station2_manual = POU.input(False)           # DI_STATION2_MANUAL
    station2_start = POU.input(False)            # DI_STATION2_START
    station2_stop = POU.input(False)             # DI_STATION2_STOP
    station3_manual = POU.input(False)           # DI_STATION3_MANUAL
    station3_start = POU.input(False)            # DI_STATION3_START
    station3_stop = POU.input(False)             # DI_STATION3_STOP
    station4_manual = POU.input(False)           # DI_STATION4_MANUAL
    station4_start = POU.input(False)            # DI_STATION4_START

    # Модуль 20
    station4_stop = POU.input(False)             # DI_STATION4_STOP
    station5_manual = POU.input(False)           # DI_STATION5_MANUAL
    station5_start = POU.input(False)            # DI_STATION5_START
    station5_stop = POU.input(False)             # DI_STATION5_STOP
    station6_manual = POU.input(False)           # DI_STATION6_MANUAL
    station6_start = POU.input(False)            # DI_STATION6_START
    station6_stop = POU.input(False)             # DI_STATION6_STOP
    station7_manual = POU.input(False)           # DI_STATION7_MANUAL

    # Модуль 21
    station7_start = POU.input(False)            # DI_STATION7_START
    station7_stop = POU.input(False)             # DI_STATION7_STOP
    station8_manual = POU.input(False)           # DI_STATION8_MANUAL
    station8_start = POU.input(False)            # DI_STATION8_START
    station8_stop = POU.input(False)             # DI_STATION8_STOP
    station9_manual = POU.input(False)           # DI_STATION9_MANUAL
    station9_start = POU.input(False)            # DI_STATION9_START
    station9_stop = POU.input(False)             # DI_STATION9_STOP

    # Модуль 22
    station10_manual = POU.input(False)          # DI_STATION10_MANUAL
    station10_start = POU.input(False)           # DI_STATION10_START
    station10_stop = POU.input(False)            # DI_STATION10_STOP
    station11_manual = POU.input(False)          # DI_STATION11_MANUAL
    station11_start = POU.input(False)           # DI_STATION11_START
    station11_stop = POU.input(False)            # DI_STATION11_STOP
    station12_manual = POU.input(False)          # DI_STATION12_MANUAL
    station12_start = POU.input(False)           # DI_STATION12_START

    # Модуль 23
    station12_stop = POU.input(False)            # DI_STATION12_STOP
    station13_manual = POU.input(False)          # DI_STATION13_MANUAL
    station13_start = POU.input(False)           # DI_STATION13_START
    station13_stop = POU.input(False)            # DI_STATION13_STOP
    station14_manual = POU.input(False)          # DI_STATION14_MANUAL
    station14_start = POU.input(False)           # DI_STATION14_START
    station14_stop = POU.input(False)            # DI_STATION14_STOP
    station15_manual = POU.input(False)          # DI_STATION15_MANUAL

    # Модуль 24
    station15_start = POU.input(False)           # DI_STATION15_START
    station15_stop = POU.input(False)            # DI_STATION15_STOP
    station16_manual = POU.input(False)          # DI_STATION16_MANUAL
    station16_start = POU.input(False)           # DI_STATION16_START
    station16_stop = POU.input(False)            # DI_STATION16_STOP
    station17_manual = POU.input(False)          # DI_STATION17_MANUAL
    station17_start = POU.input(False)           # DI_STATION17_START
    station17_stop = POU.input(False)            # DI_STATION17_STOP

    # Модуль 25
    station18_manual = POU.input(False)          # DI_STATION18_MANUAL
    station18_start = POU.input(False)           # DI_STATION18_START
    station18_stop = POU.input(False)            # DI_STATION18_STOP
    station19_manual = POU.input(False)          # DI_STATION19_MANUAL
    station19_start = POU.input(False)           # DI_STATION19_START
    station19_stop = POU.input(False)            # DI_STATION19_STOP
    station20_manual = POU.input(False)          # DI_STATION20_MANUAL
    station20_start = POU.input(False)           # DI_STATION20_START

    # Модуль 26
    station20_stop = POU.input(False)            # DI_STATION20_STOP
    station21_manual = POU.input(False)          # DI_STATION21_MANUAL
    station21_start = POU.input(False)           # DI_STATION21_START
    station21_stop = POU.input(False)            # DI_STATION21_STOP
    station22_manual = POU.input(False)          # DI_STATION22_MANUAL
    station22_start = POU.input(False)           # DI_STATION22_START
    station22_stop = POU.input(False)            # DI_STATION22_STOP
    station23_manual = POU.input(False)          # DI_STATION23_MANUAL

    # Модуль 27
    station23_start = POU.input(False)           # DI_STATION23_START
    station23_stop = POU.input(False)            # DI_STATION23_STOP
    di_reserve_5 = POU.input(False)              # DI_RESERVE_5
    di_reserve_6 = POU.input(False)              # DI_RESERVE_6
    di_reserve_7 = POU.input(False)              # DI_RESERVE_7
    di_reserve_8 = POU.input(False)              # DI_RESERVE_8
    di_reserve_9 = POU.input(False)              # DI_RESERVE_9
    di_reserve_10 = POU.input(False)             # DI_RESERVE_10

    def __init__(self):
        super().__init__()
        # Инициализация RS-триггеров для каждого оборудования
        
        # Флаг аварийного состояния
        self.emergency_stop = False

        # Ленточный питатель (M1)
        self.belt_feeder_logic = RS(
            set=lambda: self.panel1_start and not self.emergency_stop,
            reset=lambda: (self.panel1_stop or self.belt_feeder_rope_switch or self.belt_feeder_belt_break or self.emergency_stop),
            q=lambda x: setattr(self, 'belt_feeder_on', x)
        )

        # Роторный измельчитель (M2)
        self.rotary_crusher_logic = RS(
            set=lambda: self.panel2_start and not self.emergency_stop,
            reset=lambda: (self.panel2_stop or (not self.rotary_crusher_running and self.rotary_crusher_on)),
            q=lambda x: setattr(self, 'rotary_crusher_on', x)
        )

        # Конвейер КЛ-650/6000 (M3)
        self.conveyor_logic = RS(
            set=lambda: self.station1_start and not self.emergency_stop,
            reset=lambda: (self.station1_stop or self.conveyor6506000_rope_switch or self.conveyor6506000_belt_break),
            q=lambda x: setattr(self, 'conveyor6506000_crusher_on', x)
        )

        # Дробилка валковая (M4)
        self.roller_crusher_logic = RS(
            set=lambda: self.station2_start and not self.emergency_stop,
            reset=lambda: self.station2_stop or (not self.roller_crusher_running and self.roller_crusher_on),
            q=lambda x: setattr(self, 'roller_crusher_on', x)
        )

        # Конвейер КЛ-650/6000 на грохот (M5)
        self.conveyor_to_screen_logic = RS(
            set=lambda: self.station3_start and not self.emergency_stop,
            reset=lambda: self.station3_stop or self.conveyor6506000_rope_switch2 or self.conveyor6506000_belt_break2,
            q=lambda x: setattr(self, 'conveyor6506000_bolt_on', x)
        )

        # Грохот двухсеточный (M6)
        self.double_screen_logic = RS(
            set=lambda: self.station4_start and not self.emergency_stop,
            reset=lambda: self.station4_stop or (not self.double_mesh_screen_running and self.double_mesh_screen_on),
            q=lambda x: setattr(self, 'double_mesh_screen_on', x)
        )

        # Конвейер КЛ-650/6000 на бункер (M7)
        self.conveyor_to_hopper_logic = RS(
            set=lambda: self.station5_start and not self.emergency_stop,
            reset=lambda: self.station5_stop or self.conveyor6506000_rope_switch3 or self.conveyor6506000_belt_break3,
            q=lambda x: setattr(self, 'conveyor6506000_hopper_on', x)
        )

        # Конвейер КЛ-650/6000 на станцию фасовки (M8)
        self.conveyor_to_packing_logic = RS(
            set=lambda: self.station6_start and not self.emergency_stop,
            reset=lambda: self.station6_stop or self.conveyor6506000_rope_switch4 or self.conveyor6506000_belt_break4,
            q=lambda x: setattr(self, 'conveyor6506000_packing_on', x)
        )

        # Конвейер КЛ-650/10000 в сушильный барабан (M10)
        self.conveyor_to_drum_logic = RS(
            set=lambda: self.station7_start and not self.emergency_stop,
            reset=lambda: self.station7_stop or self.conveyor65010000_rope_switch or self.conveyor65010000_belt_break,
            q=lambda x: setattr(self, 'conveyor6501000_drum_on', x)
        )

        # Сушильный барабан (M11)
        self.drum_logic = RS(
            set=lambda: self.station8_start and not self.emergency_stop,
            reset=lambda: self.station8_stop or (not self.drum_running and self.drum_on),
            q=lambda x: setattr(self, 'drum_on', x)
        )

        # Вентилятор дымососа (M12)
        self.fan_logic = RS(
            set=lambda: self.station9_start and not self.emergency_stop,
            reset=lambda: self.station9_stop,
            q=lambda x: setattr(self, 'fan_on', x)
        )

        # Шнек сброса осадка (M13)
        self.sludge_auger_logic = RS(
            set=lambda: self.station10_start and not self.emergency_stop,
            reset=lambda: self.station10_stop or (not self.auger_running and self.sludge_auger_on),
            q=lambda x: setattr(self, 'sludge_auger_on', x)
        )

        # Конвейер КЛ-650/8000 после сушильного барабана (M14)
        self.conveyor_after_drum_logic = RS(
            set=lambda: self.station11_start and not self.emergency_stop,
            reset=lambda: self.station11_stop or self.conveyor6508000_rope_switch2 or self.conveyor6508000_belt_break2,
            q=lambda x: setattr(self, 'conveyor6508000_drum_on', x)
        )

        # Дробилка валковая 2 (M15)
        self.roller_crusher2_logic = RS(
            set=lambda: self.station12_start and not self.emergency_stop,
            reset=lambda: self.station12_stop or (not self.roller_crusher2_running and self.roller_crusher2_on),
            q=lambda x: setattr(self, 'roller_crusher2_on', x)
        )

        # Конвейер КЛ-650/8000 на грохот (M16)
        self.conveyor_to_screen2_logic = RS(
            set=lambda: self.station13_start and not self.emergency_stop,
            reset=lambda: self.station13_stop or self.conveyor6508000_rope_switch3 or self.conveyor6508000_belt_break3,
            q=lambda x: setattr(self, 'conveyor6508000_screen_on', x)
        )

        # Грохот двухсеточный 2 (M17)
        self.double_screen2_logic = RS(
            set=lambda: self.station14_start and not self.emergency_stop,
            reset=lambda: self.station14_stop or (not self.double_mesh_screen2_running and self.double_mesh_screen2_on),
            q=lambda x: setattr(self, 'double_mesh_screen2_on', x)
        )

        # Конвейер КЛ-650/6000 на бункер продукта фракции 3-8мм (M18)
        self.conveyor_to_bin38_logic = RS(
            set=lambda: self.station15_start and not self.emergency_stop,
            reset=lambda: self.station15_stop or self.conveyor6506000_rope_switch5 or self.conveyor6506000_belt_break5,
            q=lambda x: setattr(self, 'conveyor6506000_bin38_on', x)
        )

        # Конвейер КЛ-650/10000 на станцию фасовки (M20)
        self.conveyor_to_packing2_logic = RS(
            set=lambda: self.station16_start and not self.emergency_stop,
            reset=lambda: self.station16_stop or self.conveyor65010000_rope_switch2 or self.conveyor65010000_belt_break2,
            q=lambda x: setattr(self, 'conveyor6501000_packing2_on', x)
        )

        # Конвейер КЛ-650/6000 на бункер продукта фракции 0-2мм (M19)
        self.conveyor_to_bin02_logic = RS(
            set=lambda: self.station17_start and not self.emergency_stop,
            reset=lambda: self.station17_stop or self.conveyor6506000_rope_switch5 or self.conveyor6506000_belt_break5,
            q=lambda x: setattr(self, 'conveyor6506000_bin02_on', x)
        )

        # Шнек на переключатель потоков (M22)
        self.flow_auger_logic = RS(
            set=lambda: self.station18_start and not self.emergency_stop,
            reset=lambda: self.station18_stop or (not self.flow_auger_motion and self.flow_auger_on),
            q=lambda x: setattr(self, 'flow_auger_on', x)
        )

        # Шнек горизонтальный (M24)
        self.horizontal_auger_logic = RS(
            set=lambda: self.station19_start and not self.emergency_stop,
            reset=lambda: self.station19_stop or (not self.horizontal_auger_running and self.horizontal_auger_on),
            q=lambda x: setattr(self, 'horizontal_auger_on', x)
        )

        # Шнек вертикальный (M25)
        self.vertical_auger_logic = RS(
            set=lambda: self.station20_start and not self.emergency_stop,
            reset=lambda: self.station20_stop or (not self.vertical_auger_motion and self.vertical_auger_on),
            q=lambda x: setattr(self, 'vertical_auger_on', x)
        )

        # Шнек сброса осадка из фильтра вытяжной вентиляции (M26)
        self.vent_sludge_auger_logic = RS(
            set=lambda: self.station21_start and not self.emergency_stop,
            reset=lambda: self.station21_stop,
            q=lambda x: setattr(self, 'vent_sludge_auger_on', x)
        )

        # Вентилятор вытяжной (M27)
        self.vent_fan_logic = RS(
            set=lambda: self.station22_start and not self.emergency_stop,
            reset=lambda: self.station22_stop or (not self.vent_fan_running and self.vent_fan_on),
            q=lambda x: setattr(self, 'vent_fan_on', x)
        )

    def check_emergency_signals(self):
        """Проверка всех аварийных сигналов и отключение оборудования с высшим приоритетом"""
        # Сначала собираем ВСЕ возможные аварийные сигналы
        emergency_signals = [
            # Ленточный питатель
            self.belt_feeder_rope_switch,
            self.belt_feeder_belt_break,
            
            # Все конвейеры
            self.conveyor6506000_rope_switch,
            self.conveyor6506000_belt_break,
            self.conveyor6506000_rope_switch2,
            self.conveyor6506000_belt_break2,
            self.conveyor6506000_rope_switch3,
            self.conveyor6506000_belt_break3,
            self.conveyor6506000_rope_switch4,
            self.conveyor6506000_belt_break4,
            self.conveyor65010000_rope_switch,
            self.conveyor65010000_belt_break,
            self.conveyor6508000_rope_switch,
            self.conveyor6508000_belt_break,
            self.conveyor6508000_rope_switch2,
            self.conveyor6508000_belt_break2,
            self.conveyor6506000_rope_switch5,
            self.conveyor6506000_belt_break5,
            self.conveyor65010000_rope_switch2,
            self.conveyor65010000_belt_break2,
            
            # Датчики уровня
            self.hopper_high_level,
            self.hopper_low_level,
            self.bin38_high_level,
            self.bin38_low_level,
            self.bin02_high_level,
            self.bin02_low_level,
            self.packing_hopper_high_level,
            self.silo02_high_level,
            self.silo02_low_level
        ]

        # Проверяем наличие хотя бы одного аварийного сигнала
        if any(emergency_signals):
            print('Сработала авария', end='')
            self.emergency_stop = True
            
            # Немедленное отключение ВСЕГО критического оборудования
            # Ленточный питатель и связанное оборудование
            self.belt_feeder_on = False
            self.rotary_crusher_on = False
            self.conveyor6506000_crusher_on = False
            self.roller_crusher_on = False
            
            # Конвейеры
            self.conveyor6506000_bolt_on = False
            self.conveyor6506000_hopper_on = False
            self.conveyor6506000_packing_on = False
            self.conveyor6501000_drum_on = False
            self.conveyor6508000_drum_on = False
            self.conveyor6508000_screen_on = False
            self.conveyor6506000_bin38_on = False
            self.conveyor6506000_bin02_on = False
            self.conveyor6501000_packing2_on = False
            
            # Оборудование обработки
            self.double_mesh_screen_on = False
            self.double_mesh_screen2_on = False
            self.drum_on = False
            self.roller_crusher2_on = False
            
            # Шнеки и транспортеры
            self.sludge_auger_on = False
            self.flow_auger_on = False
            self.horizontal_auger_on = False
            self.vertical_auger_on = False
            self.vent_sludge_auger_on = False
            
            # Вентиляторы
            self.fan_on = False
            self.vent_fan_on = False
            
            # Дополнительные системы
            self.bin38_vibrator_on = False
            self.bin02_vibrator_on = False
            
            # Включение аварийной сигнализации
            # self.alarm_light = True
            # self.alarm_siren = True

            print(f'{self.belt_feeder_on, self.conveyor6501000_drum_on, self.sludge_auger_on, self.bin02_vibrator_on}')
            
            return  
        
        self.emergency_stop = False

    def main(self):
        """Основной цикл управления с генераторами"""
        t = 0

        while True:
            if t == 15:  
                self.belt_feeder_rope_switch = True
                print(f'{self.belt_feeder_rope_switch} - belt_feeder_rope_switch')

            if t == 80:  
                self.belt_feeder_rope_switch = False
                print(f'{self.belt_feeder_rope_switch} - belt_feeder_rope_switch')
            
            self.check_emergency_signals()

            # Обновляем все триггеры
            self.belt_feeder_logic()
            self.rotary_crusher_logic()
            self.conveyor_logic()
            self.roller_crusher_logic()
            self.conveyor_to_screen_logic()
            self.double_screen_logic()
            self.conveyor_to_hopper_logic()
            self.conveyor_to_packing_logic()
            self.conveyor_to_drum_logic()
            self.drum_logic()
            self.fan_logic()
            self.sludge_auger_logic()
            self.conveyor_after_drum_logic()
            self.roller_crusher2_logic()
            self.conveyor_to_screen2_logic()
            self.double_screen2_logic()
            self.conveyor_to_bin38_logic()
            self.conveyor_to_packing2_logic()
            self.conveyor_to_bin02_logic()
            self.flow_auger_logic()
            self.horizontal_auger_logic()
            self.vertical_auger_logic()
            self.vent_sludge_auger_logic()
            self.vent_fan_logic()

            t += 1

            print(f'{self.belt_feeder_on, self.conveyor6501000_drum_on, self.sludge_auger_on, self.bin02_vibrator_on}')

            if self.emergency_stop:
                print(f'[{t}] ВНИМАНИЕ! АКТИВНЫ АВАРИЙНЫЕ СИГНАЛЫ!')
            else:
                print(f'[{t}] Нормальная работа, аварийные сигналы отсутствуют')
                yield  # Возвращаем управление только в нормальном режиме

# Инициализация и привязка к физическим сигналам
control = EquipmentControl()

# Аналоговые входы
control.temp_tumble_dryer_enter = plc.AI_TEMP_TUMBLEDRYER_ENTER
control.temp_tumble_dryer_exit = plc.AI_TEMP_TUMBLEDRYER_EXIT
control.humidity_tumble_dryer_exit = plc.AI_HUMIDITY_TUMBLEDRYER_EXIT
control.ai_reserve = plc.AI_RESERVE

# Аналоговые выходы
control.temp_burner_task = plc.AO_TEMP_BURNER_TASK
control.ao_reserve = plc.AO_RESERVE

# Дискретные выходы
# Модуль 3
control.belt_feeder_on = plc.DO_BELTFEEDER_TURNON
control.rotary_crusher_on = plc.DO_ROTARYCRUSHER_TURNON
control.conveyor6506000_crusher_on = plc.DO_CONVEYOR6506000_CRUSHER_TURNON
control.roller_crusher_on = plc.DO_ROLLERCRUSHER_TURNON
control.conveyor6506000_bolt_on = plc.DO_CONVEYOR6506000_BOLT_TURNON
control.double_mesh_screen_on = plc.DO_DOUBLEMESHCSREEN_TURNON
control.conveyor6506000_hopper_on = plc.DO_CONVEYOR6506000_HOPPER_TURNON
control.hopper_gate_open_reserve = plc.DO_HOPPERGATE_OPEN_RESERVE

# Модуль 4
control.hopper_gate_close_reserve = plc.DO_HOPPERGATE_CLOSE_RESERVE
control.conveyor6506000_packing_on = plc.DO_CONVEYOR6506000_PACKING_TURNON
control.conveyor6501000_drum_on = plc.DO_CONVEYOR6501000_DRUM_TURNON
control.burner_start_allow = plc.DO_BURNER_STARTALLOW
control.burner_control_reserve = plc.DO_BURNER_CONTROL_RESERVE
control.burner_control2_reserve = plc.DO_BURNER_CONTROL2_RESERVE
control.drum_on = plc.DO_DRUM_TURNON
control.fan_on = plc.DO_FAN_TURNON

# Модуль 5
control.sludge_auger_on = plc.DO_SLUDGEAUGER_TURNON
control.filter_start_allow = plc.DO_FILTER_STARTALLOW
control.filter_control_reserve = plc.DO_FILTER_CONTROL_RESERVE
control.conveyor6508000_drum_on = plc.DO_CONVEYOR6508000_DRUM_TURNON
control.roller_crusher2_on = plc.DO_ROLLERCRUSHER2_TURNON
control.conveyor6508000_screen_on = plc.DO_CONVEYOR6508000_SCREEN_TURNON
control.double_mesh_screen2_on = plc.DO_DOUBLEMESHSCREEN2_TURNON
control.conveyor6506000_bin38_on = plc.DO_CONVEYOR6506000_BIN38_TURNON

# Модуль 6
control.bin38_vibrator_on = plc.DO_BIN38VIBRATOR_TURNON
control.bin38_gate_open_reserve = plc.DO_BIN38GATE_OPEN_RESERVE
control.bin38_gate_close_reserve = plc.DO_BIN38GATE_CLOSE_RESERVE
control.conveyor6501000_packing2_on = plc.DO_CONVEYOR6501000_PACKING_TURNON
control.conveyor6506000_bin02_on = plc.DO_CONVEYOR6506000_BIN02_TURNON
control.bin02_vibrator_on = plc.DO_BIN02VIBRATOR_TURNON
control.bin02_gate_open_reserve = plc.DO_BIN02GATE_OPEN_RESERVE
control.bin02_gate_close_reserve = plc.DO_BIN02GATE_CLOSE_RESERVE

# Модуль 7
control.flow_auger_on = plc.DO_FLOWAUGER_TURNON
control.horizontal_auger_on = plc.DO_HORIZONTALAUGER_TURNON
control.vertical_auger_on = plc.DO_VERTICALAUGER_TURNON
control.vent_filter_control_reserve = plc.DO_VENTFILTER_CONTROL_RESERVE
control.vent_filter_control2_reserve = plc.DO_VENTFILTER_CONTROL2_RESERVE
control.vent_sludge_auger_on = plc.DO_VENTSLUDGEAUGER_TURNON
control.vent_fan_on = plc.DO_VENTFAN_TURNON
control.do_reserve_1 = plc.DO_RESERVE_1

# Модуль 8
control.do_reserve_2 = plc.DO_RESERVE_2
control.do_reserve_3 = plc.DO_RESERVE_3
control.do_reserve_4 = plc.DO_RESERVE_4
control.do_reserve_5 = plc.DO_RESERVE_5
control.do_reserve_6 = plc.DO_RESERVE_6
control.do_reserve_7 = plc.DO_RESERVE_7
control.do_reserve_8 = plc.DO_RESERVE_8
control.do_reserve_9 = plc.DO_RESERVE_9

# Модуль 9
control.do_reserve_10 = plc.DO_RESERVE_10
control.do_reserve_11 = plc.DO_RESERVE_11
control.do_reserve_12 = plc.DO_RESERVE_12
control.do_reserve_13 = plc.DO_RESERVE_13
control.do_reserve_14 = plc.DO_RESERVE_14
control.do_reserve_15 = plc.DO_RESERVE_15
control.do_reserve_16 = plc.DO_RESERVE_16
control.do_reserve_17 = plc.DO_RESERVE_17

# Дискретные входы
# Модуль 10
control.belt_feeder_rope_switch = plc.DI_BELTFEEDER_ROPESWITCH_TRIPPED
control.belt_feeder_belt_break = plc.DI_BELTFEEDER_BELTBREAK_TRIPPED
control.rotary_crusher_running = plc.DI_ROTARYCRUSHER_RUNNING
control.conveyor6508000_rope_switch = plc.DI_CONVEYOR6508000_ROPESWITCH_TRIPPED
control.conveyor6508000_belt_break = plc.DI_CONVEYOR6508000_BELTBREAK_TRIPPED
control.roller_crusher_running = plc.DI_ROLLERCRUSHER_RUNNING
control.conveyor6506000_rope_switch = plc.DI_CONVEYOR6506000_ROPESWITCH_TRIPPED
control.conveyor6506000_belt_break = plc.DI_CONVEYOR6506000_BELTBREAK_TRIPPED

# Модуль 11
control.double_mesh_screen_running = plc.DI_DOUBLEMESHSCREEN_RUNNING
control.conveyor6506000_rope_switch2 = plc.DI_CONVEYOR6506000_ROPESWITCH2_TRIPPED
control.conveyor6506000_belt_break2 = plc.DI_CONVEYOR6506000_BELTBREAK2_TRIPPED
control.hopper_high_level = plc.DI_HOPPER_HIGHLEVEL
control.hopper_low_level = plc.DI_HOPPER_LOWLEVEL
control.hopper_gate_running_reserve = plc.DI_HOPPERGATE_RUNNING_RESERVE
control.hopper_gate_open_reserve_di = plc.DI_HOPPERGATE_OPEN_RESERVE
control.hopper_gate_closed_reserve = plc.DI_HOPPERGATE_CLOSED_RESERVE

# Модуль 12
control.conveyor6506000_rope_switch3 = plc.DI_CONVEYOR6506000_ROPESWITCH3_TRIPPED
control.conveyor6506000_belt_break3 = plc.DI_CONVEYOR6506000_BELTBREAK3_TRIPPED
control.packing_hopper_gate_open = plc.DI_PACKINGHOPPERGATE_OPEN
control.conveyor65010000_rope_switch = plc.DI_CONVEYOR65010000_ROPESWITCH_TRIPPED
control.conveyor65010000_belt_break = plc.DI_CONVEYOR65010000_BELTBREAK_TRIPPED
control.burner_control_reserve_di = plc.DI_BURNER_CONTROL_RESERVE
control.burner_control2_reserve_di = plc.DI_BURNER_CONTROL2_RESERVE
control.burner_control3_reserve_di = plc.DI_BURNER_CONTROL3_RESERVE

# Модуль 13
control.drum_running = plc.DI_DRUM_RUNNING
control.auger_running = plc.DI_AUGER_RUNNING
control.auger_motion = plc.DI_AUGER_MOTION
control.fan_filter_control_reserve = plc.DI_FANFILTER_CONTROL_RESERVE
control.fan_filter_control2_reserve = plc.DI_FANFILTER_CONTROL2_RESERVE
control.conveyor6508000_rope_switch2 = plc.DI_CONVEYOR6508000_ROPESWITCH2_TRIPPED
control.conveyor6508000_belt_break2 = plc.DI_CONVEYOR6508000_BELTBREAK2_TRIPPED
control.roller_crusher2_running = plc.DI_ROLLERCRUSHER2_RUNNING

# Модуль 14
control.conveyor6508000_rope_switch3 = plc.DI_CONVEYOR6508000_ROPESWITCH3_TRIPPED
control.conveyor6508000_belt_break3 = plc.DI_CONVEYOR6508000_BELTBREAK3_TRIPPED
control.double_mesh_screen2_running = plc.DI_DOUBLEMESHSCREEN2_RUNNING
control.conveyor6506000_rope_switch4 = plc.DI_CONVEYOR6506000_ROPESWITCH4_TRIPPED
control.conveyor6506000_belt_break4 = plc.DI_CONVEYOR6506000_BELTBREAK4_TRIPPED
control.bin38_high_level = plc.DI_BIN38_HIGHLEVEL
control.bin38_low_level = plc.DI_BIN38_LOWLEVEL
control.bin38_gate_running_reserve = plc.DI_BIN38GATE_RUNNING_RESERVE

# Модуль 15
control.bin38_gate_open_reserve_di = plc.DI_BIN38GATE_OPEN_RESERVE
control.bin38_gate_closed_reserve = plc.DI_BIN38GATE_CLOSED_RESERVE
control.conveyor65010000_rope_switch2 = plc.DI_CONVEYOR65010000_ROPESWITCH2_TRIPPED
control.conveyor65010000_belt_break2 = plc.DI_CONVEYOR65010000_BELTBREAK2_TRIPPED
control.packing_hopper_gate2_open = plc.DI_PACKINGHOPPERGATE2_OPEN
control.conveyor6506000_rope_switch5 = plc.DI_CONVEYOR6506000_ROPESWITCH5_TRIPPED
control.conveyor6506000_belt_break5 = plc.DI_CONVEYOR6506000_BELTBREAK5_TRIPPED
control.bin02_high_level = plc.DI_BIN02_HIGHLEVEL

# Модуль 16
control.bin02_low_level = plc.DI_BIN02_LOWLEVEL
control.bin02_gate_running_reserve = plc.DI_BIN02GATE_RUNNING_RESERVE
control.bin02_gate_open_reserve = plc.DI_BIN02GATE_OPEN_RESERVE
control.bin02_gate_closed_reserve = plc.DI_BIN02GATE_CLOSED_RESERVE
control.flow_auger_motion = plc.DI_FLOWAUGER_MOTION
control.packing_hopper_high_level = plc.DI_PACKINGHOPPER_HIGHLEVEL
control.horizontal_auger_motion = plc.DI_HORIZONTALAUGER_MOTION
control.horizontal_auger_running = plc.DI_HORIZONTALAUGER_RUNNING

# Модуль 17
control.vertical_auger_motion = plc.DI_VERTICALAUGER_MOTION
control.silo02_high_level = plc.DI_SILO02_HIGHLEVEL
control.silo02_low_level = plc.DI_SILO02_LOWLEVEL
control.vent_auger_motion = plc.DI_VENTAUGER_MOTION
control.vent_fan_running = plc.DI_VENTFAN_RUNNING
control.di_reserve_1 = plc.DI_RESERVE_1
control.di_reserve_2 = plc.DI_RESERVE_2
control.di_reserve_3 = plc.DI_RESERVE_3

# Модуль 18
control.di_reserve_4 = plc.DI_RESERVE_4
control.panel1_start = plc.DI_PANEL1_START
plc.DI_PANEL1_START.force(True)
control.panel1_stop = plc.DI_PANEL1_STOP
control.panel2_start = plc.DI_PANEL2_START
control.panel2_stop = plc.DI_PANEL2_STOP
control.station1_manual = plc.DI_STATION1_MANUAL
control.station1_start = plc.DI_STATION1_START
control.station1_stop = plc.DI_STATION1_STOP

# Модуль 19
control.station2_manual = plc.DI_STATION2_MANUAL
control.station2_start = plc.DI_STATION2_START
control.station2_stop = plc.DI_STATION2_STOP
control.station3_manual = plc.DI_STATION3_MANUAL
control.station3_start = plc.DI_STATION3_START
control.station3_stop = plc.DI_STATION3_STOP
control.station4_manual = plc.DI_STATION4_MANUAL
control.station4_start = plc.DI_STATION4_START

# Модуль 20
control.station4_stop = plc.DI_STATION4_STOP
control.station5_manual = plc.DI_STATION5_MANUAL
control.station5_start = plc.DI_STATION5_START
control.station5_stop = plc.DI_STATION5_STOP
control.station6_manual = plc.DI_STATION6_MANUAL
control.station6_start = plc.DI_STATION6_START
control.station6_stop = plc.DI_STATION6_STOP
control.station7_manual = plc.DI_STATION7_MANUAL

# Модуль 21
control.station7_start = plc.DI_STATION7_START
control.station7_stop = plc.DI_STATION7_STOP
control.station8_manual = plc.DI_STATION8_MANUAL
control.station8_start = plc.DI_STATION8_START
control.station8_stop = plc.DI_STATION8_STOP
control.station9_manual = plc.DI_STATION9_MANUAL
control.station9_start = plc.DI_STATION9_START
control.station9_stop = plc.DI_STATION9_STOP

# Модуль 22
control.station10_manual = plc.DI_STATION10_MANUAL
control.station10_start = plc.DI_STATION10_START
control.station10_stop = plc.DI_STATION10_STOP
control.station11_manual = plc.DI_STATION11_MANUAL
control.station11_start = plc.DI_STATION11_START
control.station11_stop = plc.DI_STATION11_STOP
control.station12_manual = plc.DI_STATION12_MANUAL
control.station12_start = plc.DI_STATION12_START

# Модуль 23
control.station12_stop = plc.DI_STATION12_STOP
control.station13_manual = plc.DI_STATION13_MANUAL
control.station13_start = plc.DI_STATION13_START
control.station13_stop = plc.DI_STATION13_STOP
control.station14_manual = plc.DI_STATION14_MANUAL
control.station14_start = plc.DI_STATION14_START
control.station14_stop = plc.DI_STATION14_STOP
control.station15_manual = plc.DI_STATION15_MANUAL

# Модуль 24
control.station15_start = plc.DI_STATION15_START
control.station15_stop = plc.DI_STATION15_STOP
control.station16_manual = plc.DI_STATION16_MANUAL
control.station16_start = plc.DI_STATION16_START
control.station16_stop = plc.DI_STATION16_STOP
control.station17_manual = plc.DI_STATION17_MANUAL
control.station17_start = plc.DI_STATION17_START
control.station17_stop = plc.DI_STATION17_STOP

# Модуль 25
control.station18_manual = plc.DI_STATION18_MANUAL
control.station18_start = plc.DI_STATION18_START
control.station18_stop = plc.DI_STATION18_STOP
control.station19_manual = plc.DI_STATION19_MANUAL
control.station19_start = plc.DI_STATION19_START
control.station19_stop = plc.DI_STATION19_STOP
control.station20_manual = plc.DI_STATION20_MANUAL
control.station20_start = plc.DI_STATION20_START

# Модуль 26
control.station20_stop = plc.DI_STATION20_STOP
control.station21_manual = plc.DI_STATION21_MANUAL
control.station21_start = plc.DI_STATION21_START
control.station21_stop = plc.DI_STATION21_STOP
control.station22_manual = plc.DI_STATION22_MANUAL
control.station22_start = plc.DI_STATION22_START
control.station22_stop = plc.DI_STATION22_STOP
control.station23_manual = plc.DI_STATION23_MANUAL

# Модуль 27
control.station23_start = plc.DI_STATION23_START
control.station23_stop = plc.DI_STATION23_STOP
control.di_reserve_5 = plc.DI_RESERVE_5
control.di_reserve_6 = plc.DI_RESERVE_6
control.di_reserve_7 = plc.DI_RESERVE_7
control.di_reserve_8 = plc.DI_RESERVE_8
control.di_reserve_9 = plc.DI_RESERVE_9
control.di_reserve_10 = plc.DI_RESERVE_10

def main():
    """Главный цикл программы"""
    plc.run(instances=[control], ctx=globals())

if __name__ == "__main__":
    main()