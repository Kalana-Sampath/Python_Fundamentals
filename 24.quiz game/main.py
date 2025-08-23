questions = (
    "What planet is known as the Red Planet?",
    "What gas do humans need to breathe to survive?",
    "What force keeps us on the ground?",
    "What is the center of an atom called?",
    "What is the closest star to Earth?"
)

options = (
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),             # Q1
    ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"), # Q2
    ("A. Magnetism", "B. Friction", "C. Gravity", "D. Electricity"),# Q3
    ("A. Proton", "B. Neutron", "C. Electron", "D. Nucleus"),       # Q4
    ("A. The Moon", "B. The Sun", "C. Alpha Centauri", "D. Polaris")# Q5
)

answers = ("B", "A", "C", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)  # FIXED
    
    if guess == answers[question_num]:  # FIXED
        score += 1
        print("CORRECT!")
    else: 
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1

print("--------------------------")
print("QUIZ COMPLETE!")
print(f"Your score: {score}/{len(questions)}")
