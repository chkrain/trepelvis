from pyplc.platform import plc
# from pyplc.config import hw # вызывает ошибку при выполнении программы (KRAXIO)
from collections import namedtuple
from sys import platform
from pyplc.ld import LD
import random as r
from pyplc.pou import POU
from pyplc.utils.cli import CLI
from pyplc.channel import Channel

# DI_BELTFEEDER_ROPESWITCH_TRIPPED;DI;1;1
# DI_BELTFEEDER_BELTBREAK_TRIPPED;DI;1;2

# DO_BELTFEEDER_TURNON;DO;1;1
# DO_ROTARYCRUSHER_TURNON;DO;1;2

def programm():
    if plc.DI_BELTFEEDER_ROPESWITCH_TRIPPED:
        plc.DO_BELTFEEDER_TURNON = True
        print("programm", "isTrue")
    else:
        plc.DO_BELTFEEDER_TURNON = False
        print("programm", "isFalse")
    yield
    
user_programm = LD.no(plc.DI_BELTFEEDER_BELTBREAK_TRIPPED).set(plc.DO_ROTARYCRUSHER_TURNON).end()

# telnet = CLI()
# while True:
#     telnet()

# plc.DI_BELTFEEDER_ROPESWITCH_TRIPPED.force(True)

plc.run(
    instances=
    [programm, user_programm],
    ctx=globals()
    )
