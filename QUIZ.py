def quiz():
    questions = [
        {"question": "Which colour is your fav colour?",
         "option": ["a) BLACK", "b) RED", "c) GREEN", "d) WHITE"],
         "answer": "a"
        },
        {"question": "How many planets in the solar system?",
         "option": ["a) 5", "b) 6", "c) 8", "d) 9"],
         "answer": "c"
        },
        {"question": "How many vowels in the English alphabet?",
         "option": ["a) 5", "b) 6", "c) 8", "d) 9"],
         "answer": "a"
        }
    ]
    
    score = 0
    print("Welcome to the quiz!\n")
    
    # Loop through each question
    for i, question in enumerate(questions, 1):
        print(f"Q{i}: {question['question']}")
        
        # Display options
        for option in question['option']:
            print(option)
        
        # Get user input
        user_answer = input("Enter your answer (a/b/c/d): ").lower()
        
        # Check if the answer is correct
        if user_answer == question['answer']:
            score += 1
            print("Correct!\n")
        else:
            print("Wrong answer!\n")
    
    # Display final score
    print(f"Your final score is: {score}/{len(questions)}")

# Call the quiz function
quiz()

