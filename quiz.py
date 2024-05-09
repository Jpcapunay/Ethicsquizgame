def run_quiz():
    questions = [
        {
            "question": "What is the principle of 'do no harm'?",
            "options": ["A: Causing deliberate harm", "B: Avoiding harm to others", "C: Ignoring the consequences of actions"],
            "answer": "B"
        },
        {
            "question": "Which of these is a form of ethical dilemma in professional ethics?",
            "options": ["A: Choosing between equally undesirable options", "B: Deciding on lunch", "C: Following clear legal instructions"],
            "answer": "A"
        },
        {
            "question": "What does confidentiality mean in a professional setting?",
            "options": ["A: Sharing information freely", "B: Using information for personal gain", "C: Keeping information private"],
            "answer": "C"
        }
    ]

    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (A, B, C): ").upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
        print()

    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
