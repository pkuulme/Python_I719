import random
import datetime

from questions import Add, Multiply, Subtract, Divide


class Quiz():
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Subtract, Multiply)
        # generate 10 random questions from number 1 to 20
        for _ in range(5):
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)

            question = random.choice(question_types)(num1, num2)
            # add these questions to self.questions
            self.questions.append(question)

    def take_quiz(self):
        self.start_time = datetime.datetime.now()

        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        return self.summary()


    def ask(self, question):
        correct = False
        question_start = datetime.datetime.now()

        answer = input(question.text + ' = ')
        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()

        return correct, question_end - question_start

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        print("You got {} out of {} right".format(
             self.total_correct(), len(self.questions)))

        print("It took you {} seconds".format((self.end_time - self.start_time).seconds))

    @staticmethod
    def start_quiz():
        quiz = Quiz()
        quiz.take_quiz()
