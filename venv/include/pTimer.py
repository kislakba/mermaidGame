import time
from  threading import Timer
class pTimer():
    def __init__(self,interval,handlerFunction,*arguments):
        self.interval=interval
        self.handlerFunction=handlerFunction
        self.arguments=arguments
        self.running=False
        self.timer=Timer(self.interval,self.run,arguments)
        self.isPause=False
    def start(self):
        self.running=True
        self.timer.start()
    def stop(self):
        self.running=False

    def pause(self,status=False):
        self.isPause=status
    def run(self,*arguments):
        while self.running:
            self.handlerFunction(arguments)
            time.sleep(self.interval)
            while self.isPause:
                time.sleep(0.10)
                continue


