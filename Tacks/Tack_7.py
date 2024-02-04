import random
from collections import defaultdict

import matplotlib.pyplot as plt

nums = 1_000

counts = defaultdict(int)

for _ in range(nums):
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice + dice_two] += 1

probabilities = {key: count / nums for key, count in counts.items()}

if __name__ == "__main__":
    print("Dice | Probability")
    print("-----|------------")
    for dice, prob in sorted(probabilities.items()):
        print(f"{dice} | {prob:.2%}")


    plt.bar(probabilities.keys(), probabilities.values())  # noqa
    plt.show()