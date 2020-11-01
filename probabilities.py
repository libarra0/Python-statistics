import random

def roll_dice(number_of_throws):
    throwing_sequence = []

    for _ in range(number_of_throws):
        roll = random.choice([1, 2, 3, 4, 5, 6])
        throwing_sequence.append(roll)

    return throwing_sequence

def main(number_of_throws, number_of_attempts):
    throws = []
    for _ in range(number_of_attempts):
        throwing_sequence = roll_dice(number_of_throws)
        throws.append(throwing_sequence)

    roll_1 = 0
    for throw in throws:
        if 1 not in throw:
            roll_1 += 1

    probability_throws_with_1 = roll_1 / number_of_attempts
    print(f'Probability of not getting at least 1 in {number_of_throws} throws = {probability_throws_with_1}')


if __name__ == "__main__":
    number_of_throws = int(input("How many rolls of the dice: "))
    number_of_attempts = int(input("How many times will the simulation run: "))

    main(number_of_throws, number_of_attempts)