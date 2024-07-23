from User_class import User

class Faculty (User):
    def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
        super().__init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone)
        self.set_course(course)
        self.set_occupation(occupation)
        self.set__hours(hours)
        self.set__salary(salary)
        self.set__title(title)
        self.__extra_hours = 0
        self.__extra_salary= 0

    # setters
    def set_course (self, course):
        # if isinstance(course, str):
        course = course.strip().upper()
        f = open("courses.txt")
        lines = f.readlines()
        f.close()
        for line in lines:
            list_types = line.split(" ")
        if course in list_types:
            self.__course = course
        else:
            raise ValueError("Invalid course entered")


    def set_occupation(self, occupation):
        occupation = occupation.strip().lower()
        if occupation == 'full-time' or occupation == 'part-time':
            self.__occupation = occupation
        else:
            raise ValueError("Invalid type of occupation entered")

    def set_hours(self, hours):
        extra_hours = 0
        hours = hours.strip()
        if hours.isnumeric():
           if hours >24:
               raise ValueError("It's illegal")
           elif 19 <= hours <= 24:
               self.__hours = 18
               self.__extra_hours = hours - 18
           elif 2 <= hours <= 18:
               self.__hours = hours
               self.__extra_hours = 0
           else:
               raise ValueError("You are not working at all")


    def set_title(self, title):
         title = title.strip().upper()
         f = open("titles.txt")
         lines = f.readlines()
         f.close()
         for line in lines:
             list_types = line.split(",")
         if title in list_types:
             self.__title = title
         else:
             raise ValueError("Invalid title entered")

    def set_salary(self, salary):  # Full time  / Part time  1<hours<9
        salary = {"TEACHING ASSISTANTS": 100, "LECTURERS": 150, "SENIOR LECTURERS": 200, "ASSISTANT PROFESSOR": 250,
                  "ASSOCIATE PROFESSOR": 300, "FULL PROFESSOR": 350, "ACADEMICIAN": 400}

        if salary.isdigit():
            if self.get_title() in salary.keys():
                self.__salary =  self.get_hours() * salary [self.get_title()]
                self.__extra_salary = self.get_extra_hours() * salary [self.get_title()]*2
        else:
            raise ValueError("salary must be digit")



    #getters
    def get_course(self):
        return self.__course

    def get_occupation(self):
        return self.__occupation

    def get_hours(self):        # course hours
        return self.__hours


    def  get_salary(self):
        return self.__salary

    def get_title(self):
        return self.__title

salary = input('enter')
if salary.isnumeric():
    print('correct')
else:
    print('incorrect')