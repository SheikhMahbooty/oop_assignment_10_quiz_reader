#Assignment 10 Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
#read the text file from the original quiz creator
file = open("quiz_questions.txt", "r")
f = file.readlines()
#print the quiz questions randomly
for i in range(5):
    print(f[i].strip())
#user inputs answer
#check if answer is correct
#once completed all the questions, print how many answers user got correct and ask if user wants to restart the quiz
#jump in joy