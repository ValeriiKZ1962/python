class Road:
    __length = None
    __width = None
    weight = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Create road')

    def intake(self):
        self.weight = 25
        self.thickness = 0.05
        intake = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Need {intake} ton for the road')

road_create = Road(20000, 6)
road_create.intake()