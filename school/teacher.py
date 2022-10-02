from user import User


class Teacher(User):
    type = 'Teacher'
    description = 'Describes a User'

    def __str__(self):
        return f'type: {Teacher.type} description: {Teacher.description}'
