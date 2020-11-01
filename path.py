class Path:
    def __init__(self):
        self.drunk_coordinates = {}

    def add_drunk(self, drunk, coordinate):
        self.drunk_coordinates[drunk] = coordinate

    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        current_coordinate = self.drunk_coordinates[drunk]
        new_coordinate = current_coordinate.move(delta_x, delta_y)

        self.drunk_coordinates[drunk] = current_coordinate

    def get_coordinate(self, drunk):
        return self.drunk_coordinates[drunk]