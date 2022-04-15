class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # TODO: (4) Check if questions are left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # TODO: (3) Asking the user the question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)\n").lower()
        self.check_answer(user_ans, current_question.answer)

    # TODO: (5) Check if ans correct and track score
    def check_answer(self, user_input, correct_answer):
        if user_input == correct_answer.lower():
            self.score += 1
            print(f"You got it correct!")
        else:
            print(f"You got it wrong!")

        print(f"Correct answer: {correct_answer}\nCurrent score: {self.score}/{self.question_number}\n")
