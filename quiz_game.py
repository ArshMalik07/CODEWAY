import random

#Function to show question
def show_question(question, options):
    print(question)
    #For eteration of options
    for i, option in enumerate(options,1):
        print(f"{i}. {option}")
    return int(input("Enter your answer number: "))

#Function contains quiz
def quiz():
    questions = [
        {
            "question": "What is Binary representation of 1101?",
            "options": ["10", "11", "12", "13"],
            "correct answer": 2
        },

        {
            "question": "Which keyword is used to creating the function in python?",
            "options": ["def", "define", "func", "function"],
            "correct answer": 1
        },

        {
            "question": "What is the time complexity of a linear search in an unsorted list with 'n' elements?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "correct answer": 3
        },

        {
            "question": "Which of the following is not an Object Oriented Programming language?",
            "options": ["Python", "Java", "C++", "C"],
            "correct answer": 4
        },

        {
            "question": "What keyword is used in Python to handle exceptions?",
            "options": ["catch", "try", "throw", "except"],
            "correct answer": 2
        },
    ]

    score = 0 #Initially score is zero.
    while True:
        random.shuffle(questions)#each time gives different question sequence
        for q in questions:
            answer = show_question(q['question'], q['options'])
            correct_answer = q['correct answer']

            if answer == correct_answer: # Compare actual answer with user's answer
                print("Correct!!")
                score += 1 # If correct score will increase by 1.
            else:
                print(f"Incorrect, The Correct Answer was: {q['options'][correct_answer - 1]}")# shows correct answer if answer is wrong.
        over = input("Do you want to play again? (yes/no)").lower()
        your_score = print(f"Your Score is {score} out of {len(questions)}")
        if over != 'yes':# If user want to quit.
            break

if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    quiz() #calling the quiz function
