#Ниже идет Ваша программа
from pyplc.platform import plc
from pyplc.pou import POU
from pyplc.sfc import SFC

class Logic(SFC):
  button = POU.input(False)
  power = POU.output(False)
  
  def __init__(self, button:bool = False, power: bool = False, id: str = None, parent: POU = None) -> None:
    super().__init__(id, parent)
    self.button = button
    self.power = power

  def main(self):
    yield from self.until(lambda: self.button)
    self.log('BUTTON PRESSED')
    yield from self.till(lambda: self.button)
    self.log('BUTTON RELEASED')
    self.power = True
    yield from self.until(lambda: self.button)
    self.log('BUTTON PRESSED')
    yield from self.till(lambda: self.button)
    yield from self.pause(10000)
    self.power = False

logic = Logic( button = plc.BUTTON, power = plc.CONVEYOR )
plc.run( instances=[ logic ], ctx=globals() )
