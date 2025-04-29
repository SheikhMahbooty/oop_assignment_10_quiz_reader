#Assignment 10 Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
import random
#read the text file from the original quiz creator
file = open("quiz_questions.txt", "r")
f = file.readlines()
#print the quiz questions randomly
quiz = []
for i in range(0, len(f), 6):
    if i + 5 < len(f):
        question = f[i]
        option1 = f[i+1]
        option2 = f[i+2]
        option3 = f[i+3]
        option4 = f[i+4]
        correct = f[i+5]
        quiz.append((question, [option1, option2, option3, option4], correct))

if len(quiz) == 0:
    print("No questions inputted.")
else:
    while True:
        print(f"{len(quiz)} questions are available.")
        num = int(input(f"How many questions would you like to answer? (Max: {len(quiz)}): "))
        num = min(num, len(quiz))
        
        asked = random.sample(quiz, num)
        print(asked)

#check if answer is correct
#once completed all the questions, print how many answers user got correct and ask if user wants to restart the quiz
#jump in joy