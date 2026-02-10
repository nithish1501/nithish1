class SmallObject:
    __slots__ = ("x", "y")  
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = SmallObject(1, 2)
