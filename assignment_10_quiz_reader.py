#Assignment 10 Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
import random

#read the text file from the original quiz creator
file = open("quiz_questions.txt", "r")
file_lines = file.readlines()

#initialize the options / seperate them
quiz_data = []
for line_index in range(0, len(file_lines), 6):
    if line_index + 5 < len(file_lines):
        question_text = file_lines[line_index].strip()
        option_a = file_lines[line_index + 1].strip()
        option_b = file_lines[line_index + 2].strip()
        option_c = file_lines[line_index + 3].strip()
        option_d = file_lines[line_index + 4].strip()
        correct_answer_text = file_lines[line_index + 5].strip()
        quiz_data.append((question_text, [option_a, option_b, option_c, option_d], correct_answer_text))

#check if how many questions are inputted in the txt file
if len(quiz_data) == 0:
    print("No questions inputted.")
else:
    while True:
        print(f"\n{len(quiz_data)} questions are available.")
        num_questions = int(input(f"How many questions would you like to answer? (Max: {len(quiz_data)}): "))
        num_questions = min(num_questions, len(quiz_data))
        score = 0
        selected_questions = random.sample(quiz_data, num_questions) #randomize the questions

        #enumerate the options 
        for current_question in selected_questions:
            print("\n" + current_question[0])
            choice_labels = ["A", "B", "C", "D"]

            for index, option in enumerate(current_question[1]):
                print(f"{choice_labels[index]}) {option}")

            while True:
                user_input = input("\nEnter the correct answer (a/b/c/d): ").strip().upper()
                if user_input in choice_labels:
                    break
                print("Invalid input. Please enter A, B, C, or D.")

            #check if answer is correct
            user_choice_index = choice_labels.index(user_input)
            if current_question[1][user_choice_index] == current_question[2]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {current_question[2]}")
                
        #once completed all the questions, print how many answers user got correct and ask if user wants to restart the quiz
        print(f"You got {score} out of {num_questions} correct!")
        play_again = input("Do you want to restart the quiz? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thank you for playing!")
            break