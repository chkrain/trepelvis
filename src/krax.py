from pyplc.pou import POU
from pyplc.utils import Monitor
from pyplc.platform import plc, hw, board
from sys import platform
from pyplc.utils.latch import RS

# 1. Ленточный питатель
belt_feeder = RS(
  set=lambda: hw.DI_PANEL1_START,
  reset=lambda: hw.DI_BELTFEEDER_ROPESWITCH_TRIPPED,
  q=hw.DO_BELTFEEDER_TURNON
)

# 2. Управление горелкой
def control_burner():
  if not hw.DI_BURNER_CONTROL_RESERVE:
    target_temp = 60.0
    current_temp = hw.AI_TEMP_TUMBLEDRYER_ENTER
    if current_temp < target_temp:
      power = (target_temp - current_temp) * 2
      hw.AO_TEMP_BURNER_TASK = min(max(power, 0), 100)
    else:
      hw.AO_TEMP_BURNER_TASK = 0

# 3. Аварийная остановка
def emergency_stop():
  if hw.DI_PANEL1_STOP or hw.DI_BELTFEEDER_BELTBREAK_TRIPPED:
    for attr in dir(hw):
      if attr.startswith('DO_'):
        setattr(hw, attr, False)
    hw.AO_TEMP_BURNER_TASK = 0
      
def plc_prg():
  while True:
    pass
    yield
  

instances = (plc_prg, )
if platform=="linux":
  pass
  # iauger = ...
  # instances+=(iauger,)

# if __name__ == "__main__":
#     plc.run(instances=instances, ctx=globals())

plc.run(instances=[belt_feeder, control_burner, emergency_stop], ctx=globals())

