class QuizBrain:
    def __init__(self, _input):
        self.question_number = 0
        self.question_list = _input
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, user_answer):
        if user_answer == answer:
            print("You got it right!")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong")
            print(f"The correct answer was: {answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text}: ")
        self.check_answer(current_question.answer, answer)
