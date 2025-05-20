class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self, value):
        
        return value * self.factor

three_times = Multiplier(3)
print(callable(three_times))
result = three_times(10)
print(result)