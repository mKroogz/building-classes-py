class City:
    def __init__(self):
        self.name = "Mattyville"
        self.mayor = "Matthew Kroeger"
        self.year = 2020
        self.buildings = []
        
    def construct(self, building):
        self.buildings.append(building)