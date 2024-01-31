import random
from art import logo, vs
from game_data import data

def clear():
   print("\n" * 50)

correct_answer = ""
score = 0
# first = random.randint(0, len(data))
# second  = random.randint(0, len(data))
# while first == second:
#     second = random.randint(0, len(data))

def compare(A, B):
    global correct_answer
    if data[A]['follower_count'] > data[B]['follower_count']:
       correct_answer = "A"
    #    print("A is more")
    elif data[A]['follower_count'] < data[B]['follower_count']:
       correct_answer = "B"
    #    print("B is more")
    else:
       print("Tie")

correct = True
while correct:
    clear()
    print(logo)
    if score >= 1:
        print(f"You're right! Current score: {score}")
    try:
        first
    except NameError:
        first = random.randint(0, len(data) - 1)
    second  = random.randint(0, len(data) - 1)
    while first == second:
        second  = random.randint(0, len(data) - 1)
    print(first)
    print(second)
    print(f"Compare A: {data[first]["name"]}, {data[first]["description"]}, from {data[first]['country']}.")
    print(vs)
    print(f"Compare B: {data[second]["name"]}, {data[second]["description"]}, from {data[second]['country']}.")
    compare(first, second)
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    if user_answer == correct_answer:
        score += 1
        first = second
    else:
        correct = False
        clear()
        print(f"Sorry, that's wrong. The correct answer was {correct_answer}. Final score: {score}")