class QuizBrain:
	
	def __init__(self, question_list):
		self.question_number = 0
		self.question_list = question_list
		self.correct_questions = 0
		
	def is_quiz_complete(self):
		return self.question_number == len(self.question_list)
			
	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		answer = self.is_correct(input(f"Q.{self.question_number}: {current_question.text} (True/False)?: "), current_question.answer)
		
		
	def is_correct(self, guess, answer):
		if guess.lower() == answer.lower():
			print("That's Correct!!")
			self.correct_questions += 1
		else:
			print("Sorry that's incorrect!")
		print(f"Score: ({self.correct_questions}/{self.question_number})\n")