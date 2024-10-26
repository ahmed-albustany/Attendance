from django.test import TestCase
from django.contrib.auth.models import User
from .models import Individual, Course, WaitingList
from .forms import IndividualForm, CourseForm, WaitingListForm

# Model Tests
class IndividualModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Individual.objects.create(
            id_type='Passport',
            id_number='123456789',
            name='John Doe',
            country='USA',
            phone='123-456-7890',
            sex='Male',
            family_id='F123',
            head_of_household=True,
            created_by=self.user
        )

    def test_individual_creation(self):
        individual = Individual.objects.get(id_number='123456789')
        self.assertEqual(individual.name, 'John Doe')
        self.assertEqual(individual.created_by.username, 'testuser')

class CourseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Course.objects.create(
            name='Python Course',
            age_range='18-25',
            start_date='2024-01-01',
            end_date='2024-01-31',
            description='Learn Python from scratch',
            created_by=self.user
        )

    def test_course_creation(self):
        course = Course.objects.get(name='Python Course')
        self.assertEqual(course.age_range, '18-25')
        self.assertEqual(course.created_by.username, 'testuser')

class WaitingListModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        individual = Individual.objects.create(
            id_type='Passport',
            id_number='123456789',
            name='John Doe',
            country='USA',
            phone='123-456-7890',
            sex='Male',
            family_id='F123',
            head_of_household=True,
            created_by=self.user
        )
        WaitingList.objects.create(
            id_number='123456789',
            beneficiary=individual,
            sub_category='Art',
            phone_number='123-456-7890',
            created_by=self.user
        )

    def test_waiting_list_creation(self):
        waiting_list = WaitingList.objects.get(id_number='123456789')
        self.assertEqual(waiting_list.sub_category, 'Art')
        self.assertEqual(waiting_list.created_by.username, 'testuser')

# Form Tests
class IndividualFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_valid_form(self):
        data = {
            'id_type': 'Passport',
            'id_number': '123456789',
            'name': 'John Doe',
            'country': 'USA',
            'phone': '123-456-7890',
            'sex': 'Male',
            'family_id': 'F123',
            'head_of_household': True
        }
        form = IndividualForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'id_type': '',
            'id_number': '123456789',
            'name': 'John Doe',
            'country': 'USA',
            'phone': '123-456-7890',
            'sex': 'Male',
            'family_id': 'F123',
            'head_of_household': True
        }
        form = IndividualForm(data=data)
        self.assertFalse(form.is_valid())

class CourseFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_valid_form(self):
        data = {
            'name': 'Python Course',
            'age_range': '18-25',
            'start_date': '2024-01-01',
            'end_date': '2024-01-31',
            'description': 'Learn Python from scratch'
        }
        form = CourseForm(data=data)
        self.assertTrue(form.is_valid())

class WaitingListFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.individual = Individual.objects.create(
            id_type='Passport',
            id_number='123456789',
            name='John Doe',
            country='USA',
            phone='123-456-7890',
            sex='Male',
            family_id='F123',
            head_of_household=True,
            created_by=self.user
        )

    def test_valid_form(self):
        data = {
            'id_number': '123456789',
            'beneficiary': self.individual.id,
            'sub_category': 'Art',
            'phone_number': '123-456-7890'
        }
        form = WaitingListForm(data=data)
        self.assertTrue(form.is_valid())