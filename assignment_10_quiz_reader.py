#Assignment 10 Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
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
    
for i in range(5):
    print(f[i].strip())
for i in range(5, 6):
    print(f[i].strip())
    
#user inputs answer
answer = input("\nEnter the correct answer: ")

#check if answer is correct
#once completed all the questions, print how many answers user got correct and ask if user wants to restart the quiz
#jump in joy