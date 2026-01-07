print('     ------ Hii 👋🏻------\n')
print('Welcome to the Quiz Game\n ')

print('🔸 in this game. you will be presented five randomly selected multiple-choice questions \nfrom a predefined question file.\n'
'each question will have four answer options,\nand you used to choose the one '
'that best fits the question. 🔸\n')

name=input('First enter your name : \n' ).upper()

print(f'    ---------🏆🏆 We wish you the best of luck {name}, congratulation on taking on the challenge 🏆🏆---------\n')

# Import random module for question selection
import random
"""
    Load questions from a specified file.
    
    The file should have each question in the format:
    Question text|Option A|Option B|...|Correct Answer"""
def readfile(filename="Question.txt"):
    questions = []
        # Open file in read mode (automatically closes when done)
    with open(filename, 'r') as file:
            lines = file.readlines()
            numofline=len(lines)
        # Process questions in groups of 6 lines (1 question + 4 options + 1 answer)
    for i in range(0,numofline,6):
        if i + 5 < numofline:
            text = lines[i]
            options = lines[i+1:i+5]
            answer = lines[i+5].strip()
            questions.append((text,options,answer))
    return questions

def run_question(question_data):
    # Unpack question components
    text,options,answer = question_data
    print(text)
    for opt in options:
        print(opt)
        # Get user's answer and standardize it (uppercase, no whitesp
    your_answer = input('Enter your answer like (A/B/C/D): ').strip().upper()
        # Check if answer is correct
    if your_answer == answer:
        print('☑️ correct!\n')
        return True
    else:
        print(f'correct answer is {answer} so ❌ incorrect answer \n')
        return False
    
def random_quiz():
    questions = readfile()
       # Select 5 random questions (or fewer if not enough available)
    selected_question=random.sample(questions,min(5,len(questions)))
            
    score=0
    # Ask each selected question
    for question in selected_question:
        if run_question(question):
            score+=20
    print(f'your final score is :{score}/100')
    print(f'🏆 {name} Thank you for participate so congratulation 🏆')
random_quiz()
        
        