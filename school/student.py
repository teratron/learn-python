from user import User


class Student(User):
    type = 'Student'
    description = 'Describes a User'

    def __init__(self, first_name='', last_name='', email='', password=''):
        super().__init__(first_name, last_name, email, password)
        self.email = None

    def __str__(self):
        return f'type: {Student.type} description: {Student.description}'
