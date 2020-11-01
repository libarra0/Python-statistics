import random
import math

def mean(X):
    return sum(X) / len(X)

def variance(X):
    mu = mean(X)

    accumulator = 0
    for x in X:
        accumulator += (x - mu)**2

    return accumulator / len(X)

def standard_deviation(X):
    return math.sqrt(variance(X))

def run():
    X = [random.randint(9, 12) for i in range(20)]
    mu = mean(X)
    var = variance(X)
    sigma = standard_deviation(X)

    
    print(f'X Array = {X}')
    print(f'Mean = {mu}')
    print(f'Variance = {var}')
    print(f'Standar deviation = {sigma}')


if __name__ == "__main__":
    run()