from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank[0].text)
quiz.question_number += 1
print(f"Q.{quiz.question_number}: {quiz.question_list} (True/False)?: ")

