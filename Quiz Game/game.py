# 10/02/2025

from questions import questions

score = 0

player_name = input("Enter a user name to start playing: ")

welcome = input(f"Welcome {player_name}\nPress Enter to start ...\n")

for question in questions:
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    user_answer = input("Your answer: ").upper()
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"Your score is {score}/{len(questions)}")
