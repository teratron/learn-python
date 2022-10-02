import student
import user

if __name__ == '__main__':
    _user = user.User(first_name='John', last_name='Doe', email='john@example.com')
    print(_user.first_name)

    _student = student.Student()
    print(_student.type)
    print(_student.description)
    print(_student.email)
    print(_student)
