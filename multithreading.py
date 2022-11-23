# Multithreading is a way of running multiple threads in parallel

import threading
import time

class CPUPainter:
    
    def paint_wall(self):
        time.sleep(2)
        print("Wall painted")
        
    def __init__(self):
        t = threading.Thread(target=self.paint_wall)
        t.start()
        
CPUPainter()   
CPUPainter()   
CPUPainter()   
CPUPainter()   