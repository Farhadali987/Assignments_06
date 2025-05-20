class Engine:
    def start(self):
        print("start engine")

class Car:
    def __init__(self,engine):
        self.engine = engine
    
    def start_engine(self):
        self.engine.start()

engine = Engine()
my_car = Car(engine)
my_car.start_engine()