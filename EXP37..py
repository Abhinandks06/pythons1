class Time:
    def __init__(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def __add__(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=Time(2,10,5)
print("Time 1 = 2hours 10minutes & 5 seconds")
o2=Time(4,5,10)
print("Time 2 = 4hours 5minutes & 10 seconds")
print("Adding both times")
print(o1+o2)