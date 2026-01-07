import random

counter = 0

for _ in range(10000):
    # flips = []

    # for _ in range(100):
    #     if random.randint(0, 1) == 0:
    #         flips.append('H')
    #     else:
    #         flips.append('T')

    flips = ['H' if random.randint(0, 1) == 0 else 'T' for _ in range(100)]

    streak = 3
    for i in range(len(flips)):
        if flips[i:i + streak] == [flips[i]] * streak:
            counter += 1

print(f"{(counter / 10000):.2f}% chance of a streak of {streak} in a row\n")
