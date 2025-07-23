from pyplc.platform import plc
# from pyplc.config import hw # вызывает ошибку при выполнении программы (KRAXIO)
from collections import namedtuple
from sys import platform
from pyplc.ld import LD
from pyplc.pou import POU
from pyplc.utils.cli import CLI
from pyplc.channel import Channel

def programm():
    if plc.DI_BELTFEEDER_ROPESWITCH_TRIPPED:
        plc.DO_BELTFEEDER_TURNON = True
        print("programm", "isTrue")
    else:
        plc.DO_BELTFEEDER_TURNON = False
        print("programm", "isFalse")
    yield
    
def user_programm():
    if plc.DI_BELTFEEDER_BELTBREAK_TRIPPED:
        plc.DO_ROTARYCRUSHER_TURNON = True
        print("user_programm", "isTrue")
    else:
        plc.DO_ROTARYCRUSHER_TURNON = False
        print("user_programm", "isFalse")
    yield

# telnet = CLI()
# while True:
#     telnet()

plc.DI_BELTFEEDER_ROPESWITCH_TRIPPED.force(True)

plc.run(
    instances=
    [programm, user_programm],
    ctx=globals()
    )
