class Map:
    def __init__(self, x, y):
        self.x_range = range(1, x)
        self.y_range = range(1, y)


test = Map(10)
print(test.x_range)
