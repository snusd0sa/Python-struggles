# create a question class with two attributes: text and answer
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_question = Question("2+2", "4")
print(new_question.text)
print(new_question.answer)
