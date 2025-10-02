# 10/02/2025

from questions import questions

for question in questions:
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    user_answer = input("Your answer: ").upper()
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print("Wrong!")
