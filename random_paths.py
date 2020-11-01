from drunk import TraditionalDrunk
from path import Path
from coordinates import Coordinates

from bokeh.plotting import figure, show

def hike(path, drunk, steps):
    start = path.get_coordinate(drunk)

    for _ in range(steps):
        path.move_drunk(drunk)

    return start.new_distance(path.get_coordinate(drunk))


def simulate_walk(steps, number_of_attempts, kind_of_drunk):
    drunk = kind_of_drunk(name = "Leonardo")
    origin = Coordinates(0, 0)
    distances = []

    for _ in range(number_of_attempts):
        path = Path()
        path.add_drunk(drunk, origin)
        simulate_walk = hike(path, drunk, steps)
        distances.appgitend(round(simulate_walk, 1))

    return distances


def graph(x, y):
    graph = figure(title="Random path", x_axis_label="steps", y_axis_label="distance")
    graph.line(x, y, legend="Mean distance")

    show(graph)


def main(distance_of_walk, number_of_attempts, kind_of_drunk):
    mean_distance_per_hike = []

    for steps in distance_of_walk:
        distances_walk = simulate_walk(steps, number_of_attempts, kind_of_drunk)
        mean_distance = round(sum(distances_walk) / len(distances_walk), 4)
        maxim_distance = max(distances_walk)
        minim_distance = min(distances_walk)
        mean_distance_per_hike.append(mean_distance)
        print(f'{kind_of_drunk.__name__} random walk of the {steps}')
        print(f'Mean = {mean_distance}')
        print(f'Max = {maxim_distance}')
        print(f'Min = {minim_distance}')

    graph(distance_of_walk, mean_distance_per_hike)


if __name__ == "__main__":
    distance_of_walk = [10, 100, 1000, 10000]
    number_of_attempts = 100

    main(distance_of_walk, number_of_attempts, TraditionalDrunk)