# 10/02/2025

from questions import questions

score = 0

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
print(f"Your score is {score}")
