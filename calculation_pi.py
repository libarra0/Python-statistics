import random
import math
from statistics import stdev, mean


def throw_needles(needles_number):
    inside_the_circle = 0

    for _ in range(needles_number):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distance_from_the_center = math.sqrt(x ** 2 + y ** 2)

        if distance_from_the_center <= 1:
            inside_the_circle += 1

    return (4 * inside_the_circle) / needles_number

def estimate(needles_number, attempts):
    estimates = []

    for _ in range(attempts):
        estimate_pi = throw_needles(needles_number)
        estimates.append(estimate_pi)

    estimated_mean = mean(estimate)
    sigma = stdev(estimate)
    print(f'Est = {round(estimated_mean, 5)} sigma = {round(sigma, 5)}, needles = {needles_number}')

    return (estimated_mean, sigma)

def estimate_pi(precision, attempts):
    needles_number = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        mean, sigma = estimate(needles_number, attempts)
        needles_number *= 2

    return mean


if __name__ == "__main__":
    estimate_pi(0.01, 1000)