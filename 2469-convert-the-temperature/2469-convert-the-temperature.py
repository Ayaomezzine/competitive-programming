from typing import List
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
      
        if not (0 <= celsius <= 1000):
            raise ValueError("Input temperature must be between 0 and 1000 degrees Celsius.")

        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round(celsius * 1.80 + 32.00, 5)

        return [kelvin, fahrenheit]

