from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

num_questions = input("How many questions do you want? ")
difficulty = input("Select a difficulty, easy, medium or hard: ")
question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data(num_questions, difficulty)]

quiz = QuizBrain(question_bank)
while not quiz.is_quiz_complete():
	quiz.next_question()
	
print("\nThe quiz is over.")
print(f"You got {quiz.correct_questions} questions right out of a possible {quiz.question_number}")
percentage = round(quiz.correct_questions * 100 / quiz.question_number)
print(f"You scored {percentage}%")