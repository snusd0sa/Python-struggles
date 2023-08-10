class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new = Question("text", "answer")
print(new.text)

from selenium import webdriver
chrome_driver_path = "C:\Development\chromedriver.exe"