import openai
from User_class import User
from Faculty_class_test import Faculty


class LMS (Faculty):
    def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title, e_tutor):
        super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title)
        self.set_e_tutor()


    def set_e_tutor(self, e_tutor):
        self.__e_tutor = e_tutor


    def get_e_tutor(self):
        return self.__e_tutor

if __name__ == "__main__":


