#Assignment 9: Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

#Make python create a txt file and if user adds more questions, update the file every time a new question gets added
quiz_file = open("quiz_questions.txt", "a")

#Create loop so the user can input a question
while True:
    input_question = input("\nEnter a question or type 'exit' to exit: ") #Created question loop to exit or add a question
    if input_question.lower() == "exit":
        break

#Input variables for each answer
    answer_a = input("Enter answer a: ")
    answer_b = input("Enter answer b: ")
    answer_c = input("Enter answer c: ")
    answer_d = input("Enter answer d: ")
    
#Input for the correct answer
    while True:
        correct_ans = str(input("\nCorrect answer (a/b/c/d): "))
        if correct_ans == "a":
            correct_ans = answer_a
            break
        elif correct_ans == "b":
            correct_ans = answer_b
            break
        elif correct_ans == "c":
            correct_ans = answer_c
            break
        elif correct_ans == "d":
            correct_ans = answer_d
            break
        else:
            correct_ans = print("\nInvalid input, enter a,b,c,d")

#Write the text within the txt file
    quiz_file.write(f"Question: {input_question}\n")
    quiz_file.write(f"a) {answer_a}\n")
    quiz_file.write(f"b) {answer_b}\n")
    quiz_file.write(f"c) {answer_c}\n")
    quiz_file.write(f"d) {answer_d}\n")
    quiz_file.write(f"Correct Answer: {correct_ans}\n\n")

#Print the question and answers to the shell for easier access
    print("\nThe inputted question is: ",input_question)
    print("a.",answer_a)
    print("b.",answer_b)
    print("c.",answer_c)
    print("d.",answer_d)
    print("The correct answer is: ",correct_ans)
    print("Note: the txt file will update if you exit the program, if you continue it will write a new question")

#Close the file
quiz_file.close()