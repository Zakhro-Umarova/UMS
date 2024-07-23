from User_class import User
import abc


class Faculty(User):
    def __init__(self, type, name, pass_id, email, date_of_birth, gender, nationality, phone, course, occupation, hours, salary, title):
        super().__init__(type, name, pass_id, email, date_of_birth, gender, nationality, phone)
        self.set_course(course)
        self.set_occupation(occupation)
        self.set_hours(hours)
        self.set_salary(salary)
        self.set_title(title)

        self.__titles={"TEACHING ASSISTANTS": 1, "LECTURERS": 1.5, "SENIOR LECTURERS": 2, "ASSISTANT PROFESSOR": 2.5, "ASSOCIATE PROFESSOR": 3, "FULL PROFESSOR": 3.5, "ACADEMICIAN": 4}
        self.__extra_hours = 0
        self.__extra_salary = 0

    # setters
    def set_course(self, course):
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
        if occupation == 'full-time':
            self.__occupation = 1
        elif occupation == 'part-time':
            self.__occupation = 0.5
        else:
            raise ValueError("Invalid type of occupation entered")

    def set_hours(self, hours):
        hours = hours.strip()
        if hours.isnumeric():
            if self.__occupation == 1:
                if int(hours) > 24:
                    raise ValueError("It's illegal")
                elif 19 <= int(hours) <= 24:
                    self.__hours = 18
                    self.__extra_hours = int(hours) - 18
                elif 2 <= int(hours) <= 18:
                    self.__hours = int(hours)
                    self.__extra_hours = 0
                else:
                    raise ValueError("You are not working at all")
            elif self.__occupation == 0.5:
                if int(hours) > 12:
                    raise ValueError("It's illegal")
                elif 10 <= int(hours) <= 12:
                    self.__hours = 9
                    self.__extra_hours = int(hours) - 9
                elif 1 <= hours <= 9:
                    self.__hours = int(hours)
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

    def set_salary(self, salary):


        if salary.isnumeric():
            if self.__title in self.__titles.keys():
                self.__salary = (salary / self.__hours * self.__occupation ) + self.__extra_hours * 2 * (salary / self.__hours)

        else:
            raise ValueError("salary must be numeric")

    # getters
    def get_course(self):
        return self.__course

    def get_occupation(self):
        return self.__occupation

    def get_hours(self):
        return self.__hours

    def get_salary(self):
        return self.__salary

    def get_title(self):
        return self.__title

    def teaches(self):
        pass

if __name__ == "__main__":
    faculty = Faculty('Staff', "Alice", 'AA1234567', 'alice@gmail.com', '2023/02/10', 'female', 'russian', '998901234567', "python", 'full-time', '10', '100', "LECTURER")