class FourCal:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):
    def double(self):
        return self.first * self.second


a = MoreFourCal(2,4)
print(a.add())
print(a.double())
a.second=1
print(a.add())