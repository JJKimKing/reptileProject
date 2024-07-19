import json


class Person:
    def __init__(self, data=None):
        self._name = "1"
        self._sex = ""
        self._blood_type = "O"
        self._hobbies = []
        self._date_of_birth = "1900/1/1"
        if data:
            self._name = data.get('name', self._name)
            self._sex = data.get('sex', self._sex)
            self._blood_type = data.get('blood_type', self._blood_type)
            self._hobbies = data.get('hobbies', self._hobbies)
            self._date_of_birth = data.get('date_of_birth', self._date_of_birth)

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date):
        self._date_of_birth = date

    def __str__(self):
        return (f'Person=(name={self._name},sex={self._sex},'
                f'blood_type={self._blood_type},hobbies={self._hobbies},date_of_birth={self._date_of_birth})')


def main():
    str1 = '{"name": "Tom", "sex": "male", "blood_type": "A", "hobbies": ["篮球", "足球"]}'
    person = json.loads(str1, object_hook=Person)
    print(person.date_of_birth)
    person.date_of_birth = "2014/07/02"
    print(person)


if __name__ == '__main__':
    main()
