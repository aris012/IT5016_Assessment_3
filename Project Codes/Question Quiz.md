## Question quiz
### A python program that uses a function to evaluate answers and return the code.

#### Below is the sample python code challenge. 

##### Put the questions you want to ask with giving the value of question, put the choices on the value of the options

        questions = ("What mammal has the most powerful bite?: ",
                     "What is the fastest sea animal?: ",
                     "Which bird’s eye is bigger than its brain?: ")


        options = (("A. Lion", "B. Hippopotamus", "C. Crocodile"),
                   ("A. Dolphin", "B. Tuna", "C. Sailfish",),
                   ("A. Ostrich", "B. Owl", "C. Eagle"))

##### Input the correct answers

        answers = ("B", "C", "A")
        guesses = []
        score = 0
        question_num = 0

##### For the question and answer output code

        for question in questions:
            print("---------------------")
            print(question)
            for option in options[question_num]:
                print(option)            


            guess = input("Enter (A, B, C): ").upper()
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[question_num]} is the correct answers")
            question_num += 1

##### Output Result

        print("---------------------")
        print("      RESULTS        ")
        print("---------------------")


        print("answers: ", end="")
        for answer in answers:
            print(answer, end=" ")
        print()


        print("guesses: ", end="")
        for guess in guesses:
            print(guess, end=" ")
        print()


        score = int(score / len(questions) * 100)
        print(f"Your score is: {score}%")
