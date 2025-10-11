# 10/02/2025

from questions import questions
import csv
import os

score = 0
def play_quiz():
    global score
    print("Function has started")
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

    if not os.path.exists("scores.csv"):
            with open("scores.csv", "w", newline="") as scores_file:
                writer = csv.writer(scores_file)
                writer.writerow(["Player name", "Score"])

    # Write score to csv file
    with open("scores.csv", "a") as scores_file:
        writer = csv.writer(scores_file)
        writer.writerow([player_name, score])

if __name__ == "__main__":
    play_quiz()