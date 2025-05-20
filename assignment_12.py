class TemperatureConvertor:
    @staticmethod
    
    def celsius_to_fahrenhiet(c):
       
        return (c * 9/5) + 32


converter = TemperatureConvertor()
print("0°C =", converter.celsius_to_fahrenhiet(0), "°F")