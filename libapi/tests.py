from django.test import TestCase
from libapi.models import Student
from libapi.forms import ContactForm

# Create your tests here.
class ContactFormTestCase(TestCase):
    def test_validation(self):
        c = ContactForm()
        self.assertFalse(c.is_valid(), 'Validation fails')

        data = {
            'email': 'mehul@gmail.com',
            'message': 'kjfg gdkf g fdgj  kfdg g k gfdkgfg fgk fg dfkg dfkg dfkjg kfdg kfdg kdfg kdf g'
        }
        c = ContactForm(data=data)
        self.assertTrue(c.is_valid(), 'Validation passes')

        data = {
            'email': 'mehul@',
            'message': 'kjfg gdkf g fdgj  kfdg g k gfdkgfg fgk fg dfkg dfkg dfkjg kfdg kfdg kdfg kdf g'
        }
        c = ContactForm(data=data)
        self.assertFalse(c.is_valid(), 'Validation fails')
        self.assertEqual(c['email'].errors[0], 'Hey, enter right format email')

        data = {
            'email': 'mehul@gmail.com',
            'message': 'Hi hello'
        }
        c = ContactForm(data=data)
        self.assertFalse(c.is_valid(), 'Validation fails')
        self.assertEqual(c['message'].errors[0], 'Please be elaborate!')

        data = {
            'email': 'mehul@gmail.com',
            'message': 'Hi hello fg fdgkl dgldfk fdlgkndf dfgklndf dflgkndf ldfng'
        }
        c = ContactForm(data=data)
        self.assertFalse(c.is_valid(), 'Validation fails')
        self.assertEqual(c['message'].errors[0], 'Please be elaborate!')

        data = {
            'email': 'mehul@gmail.com',
            'message': 'Hi hello fg fdgkl dgldfk fdlgkndf dfgklndf dflgkndf ldfng fdgjndf'
        }
        c = ContactForm(data=data)
        self.assertTrue(c.is_valid(), 'Validation passes')

class StudentModelTestCase(TestCase):

    def get_actual_grade(self, student_data):
        s = Student.objects.create(**student_data)
        return s.get_grade()

    def test_get_grade(self):
        student_data = {
            'name': 'mehul',
            'gender': 'm',
            'roll': 10,
            'marks': 73
        }

        expected = 'A'
        actual = self.get_actual_grade(student_data)

        self.assertEqual(actual, expected, 'the get_grade() returns A for marks 73')

        marks_to_check = [(62, 'B'), (46, 'C'), (32, 'F'), (101, 'I'), (-34, 'I')]
        for marks, expected in marks_to_check:
            student_data['marks'] = marks
            actual = self.get_actual_grade(student_data)

            self.assertEqual(actual, expected)

    def test_get_males(self):
        student_list = [
            {
                'name': 'mehul',
                'gender': 'm',
                'roll': 10,
                'marks': 73
            },
            {
                'name': 'jane',
                'gender': 'f',
                'roll': 11,
                'marks': 80
            },
            {
                'name': 'mark',
                'gender': 'm',
                'roll': 12,
                'marks': 90
            }
        ]

        for student in student_list:
            s = Student.objects.create(**student)

        males = Student.get_males()
        self.assertIsNotNone(males)
        expected = 2
        actual = len(males)

        self.assertEqual(actual, expected)

    def test_get_males_when_none(self):
        student_list = [
            {
                'name': 'jane',
                'gender': 'f',
                'roll': 11,
                'marks': 80
            }
        ]

        for student in student_list:
            s = Student.objects.create(**student)

        males = Student.get_males()
        self.assertIsNotNone(males)
        expected = 0
        actual = len(males)

        self.assertEqual(actual, expected)
