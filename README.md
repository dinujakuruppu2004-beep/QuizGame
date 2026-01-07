PYTHON QUIZ GAME


Description:

* A command-line based quiz game that presents users with 5 random multiple-choice questions from a predefined question bank. The game keeps score and provides immediate feedback for each answer.
 
Features:

* Simple and interactive command-line interface
* Random question selection for each game session
* Immediate feedback on answers (correct/incorrect)
* Score tracking (20 points per correct answer)
* Case-insensitive answer input


File Structure:

* main.py       : Main game script
* Question.txt  : Question bank file (must be in same directory)

Question File Format:

Each question must be formatted as 6 consecutive lines:
1. Question text
2. Option A
3. Option B
4. Option C
5. Option D
6. Correct answer (A/B/C/D)

Example:
10. Which method adds an element to the end of a list?  
 A) list.insert()  
 B) list.append()  
 C) list.add()  
 D) list.push()  
 B  

How to Run:

1. Ensure Python is installed
2. Place Question.txt in same directory as main.py
3. Run command: python main.py

Game Flow:

1. User enters their name
2. Game displays instructions
3. 5 random questions are presented one by one
4. After each answer, immediate feedback is given
5. Final score is displayed (out of 100)

Scoring:

* Each correct answer: +20 points
* Maximum possible score: 100 points


To modify the game:
* Edit Question.txt to add/change questions
* Change number of questions by modifying the min() parameter in random_quiz()
* Adjust scoring by changing the point value in the score+=20 line

Enjoy the game!

[AF/23/0160]
