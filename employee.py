import json


class Employee:
    def __init__(
        self, first_name, last_name, father_name, national_code, phone
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.national_code = national_code
        self.phone = phone

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def father_name(self):
        return self.__father_name

    @father_name.setter
    def father_name(self, father_name):
        self.__father_name = father_name

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, national_code):
        self.__national_code = national_code

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    def __repr__(self) -> str:
        return "Employee({},{},{},{},{})".format(
            self.first_name,
            self.last_name,
            self.father_name,
            self.national_code,
            self.phone,
        )

    def __str__(self):
        return f"Frist Name: {self.first_name}\nLast Name: {self.last_name}\nFather Name: {self.father_name}\nNational Code: {self.national_code}\nPhone: {self.phone}"

    def export(self):
        data = dict()
        data["first_name"] = self.first_name
        data["last_name"] = self.last_name
        data["father_name"] = self.father_name
        data["national_code"] = self.national_code
        data["phone"] = self.phone

        return json.dumps(data)
