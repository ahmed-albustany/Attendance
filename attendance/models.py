from django.db import models

class Individual(models.Model):
    id_type = models.CharField(max_length=50)  # e.g., Passport, National ID
    id_number = models.CharField(max_length=50)  # Individual ID number
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    sex = models.CharField(max_length=10)  # e.g., Male, Female
    family_id = models.CharField(max_length=50)  # Family ID or Head of Household ID
    head_of_household = models.BooleanField(default=False)  # True or False

    def __str__(self):
        return f"{self.name} ({self.id_number})"

class WaitingList(models.Model):
    id = models.AutoField(primary_key=True)  # Auto increment key
    id_number = models.CharField(max_length=100)  # ID number for the individual
    beneficiary = models.ForeignKey(Individual, on_delete=models.CASCADE)  # Foreign key to Individual
    application_date = models.DateTimeField(auto_now_add=True)  # Include time
    sub_category = models.CharField(max_length=100, choices=[('Art', 'Art'), ('English', 'English'), ('Arabic', 'Arabic')])  # Category
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"WaitingList: {self.id} - {self.beneficiary.name}"

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age_range = models.CharField(
        max_length=10,
        choices=[('12-14', '12-14'), ('15-18', '15-18')]  # Corrected syntax
    )
    age_range = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name