import random
import datetime

from questions import Add, Multiply, Subtract, Divide


class Quiz():
  

    def __init__(self):
        self.questions = []
        self.answers = []
        question_types = (Add, Subtract, Multiply)
        
        # generate 10 random questions from number 1 to 20
        for _ in range(5):
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)

           

            question = random.choice(question_types)(num1, num2)
            # add these questions to self.questions
            self.questions.append(question)

    def take_quiz(self):
        #log the start time
        self.start_time = datetime.datetime.now()
        #ask all the questions
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        return self.summary()


    def ask(self, question):
        correct = False
        #log the start time
        question_start = datetime.datetime.now()
        #Capture the answer
        answer = input(question.text + ' = ')
        #check the answer
        if answer == str(question.answer):
            correct = True
        #log the end time
        question_end = datetime.datetime.now()
        #Return the amount of correct answers and time it took
        return correct, question_end - question_start

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        #Print the amount of correct answers
        print("You got {} out of {} right".format(
             self.total_correct(), len(self.questions)))
        #Print the time it took to answer the questions
        print("It took you {} seconds".format((self.end_time - self.start_time).seconds))

    #Initiates the program

def start_quiz():
    quiz = Quiz()
    quiz.take_quiz()


if __name__=='__main__':
    start_quiz()