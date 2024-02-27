from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.data = defaultdict(int)
        self.f = defaultdict(int)

    def add(self, number: int) -> None:
        if self.f[self.data[number]] != 0:
            self.f[self.data[number]] -= 1
        self.data[number] += 1
        self.f[self.data[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.data[number] > 0:
            self.f[self.data[number]] -= 1
            self.data[number] -= 1
            self.f[self.data[number]] += 1

        

    def hasFrequency(self, frequency: int) -> bool:
        return self.f[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)