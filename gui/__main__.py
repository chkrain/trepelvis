import sys
from pysca import app
from pysca.device import PYPLC
import pygui.multihead as navbar

def main():
    import argparse
    args = argparse.ArgumentParser(sys.argv)
    args.add_argument('--device', action='store', type=str, default='192.168.8.10', help='IP address of the device')
    args.add_argument('--simulator', action='store_true', default=False, help='Same as --device 127.0.0.1')
    ns = args.parse_known_args()[0]
    if ns.simulator:
        ns.device = '127.0.0.1'
        import subprocess
        logic = subprocess.Popen(["python3", "src/krax.py"])
    
    dev = PYPLC(ns.device)
    app.devices['PLC'] = dev
    
    Main = app.window('ui/main.ui')
    Second = app.window('ui/Home.ui')
    
    # с использованием navbar
    navbar.append(Main)
    navbar.append(Second)       
    navbar.instance.show( )
    navbar.instance.setWindowTitle('APP MY')
    # или 
    
    # Main.show()               
    # Second.show()
    
    dev.start(100)
    app.start( ctx = globals() )
    dev.stop( )

    if ns.simulator:
        logic.terminate( )
        pass

if __name__=='__main__':
    main( )
    