#Assignment 10 Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
import random

#read the text file from the original quiz creator
file = open("quiz_questions.txt", "r")
f = file.readlines()

#initialize the options / seperate them
quiz = []
for i in range(0, len(f), 6):
    if i + 5 < len(f):
        question = f[i].strip()
        option1 = f[i+1].strip()
        option2 = f[i+2].strip()
        option3 = f[i+3].strip()
        option4 = f[i+4].strip()
        correct = f[i+5].strip()
        quiz.append((question, [option1, option2, option3, option4], correct))

#check if how many questions are inputted in the txt file
if len(quiz) == 0:
    print("No questions inputted.")
else:
    while True:
        print(f"{len(quiz)} questions are available.")
        num = int(input(f"How many questions would you like to answer? (Max: {len(quiz)}): ")) #give user an option to choose how many questions
        num = min(num, len(quiz))
        score = 0
        asked = random.sample(quiz, num) #randomize the questions

        #enumarate the options 
        for q in asked:
            print("\n" + q[0])
            letters = ["A", "B", "C", "D"]
            for i, opt in enumerate(q[1]):
                print(f"{letters[i]}) {opt}")
            while True:
                answer = input("\nEnter the correct answer (a/b/c/d): ").strip().upper() #input the correct answer
                if answer in letters:
                    break
                print("Invalid input. Please enter a, b, c, or d.")

            #check if answer is correct
            index = letters.index(answer)
            if q[1][index] == q[2]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q[2]}")
                
        #once completed all the questions, print how many answers user got correct and ask if user wants to restart the quiz
        print(f"You got {score} out of {num} correct!")
        again = input("Do you want to restart the quiz? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for playing") #jump in joy
            break