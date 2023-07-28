from art import logo, vs
from game_data import data

import random
import os

score = 0
# game_over = False


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def compare_followers(compare_a, compare_b):
    if compare_a["follower_count"] > compare_b["follower_count"]:
        return "a"
    else:
        return "b"


compare_a = random.choice(data)
compare_b = random.choice(data)


print(logo)
if score > 0:
    print(f"You're right! Current score: {score}.")
print(
    f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}."
)
print(vs)
print(
    f"Against: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}."
)
input("Who has more followers? Type 'A' or 'B': ").lower()


# print(data)
