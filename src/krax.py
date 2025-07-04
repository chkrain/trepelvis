#Ниже идет Ваша программа
from pyplc.platform import plc
from sys import platform

def plc_prg():
  while not plc.AUGER: yield
  print('OK')
  while plc.AUGER: yield
  print('DONE')

instances = (plc_prg, )
if platform=="linux":
  pass
  # iauger = ...
  # instances+=(iauger,)

plc.run( instances=instances, ctx=globals() )
