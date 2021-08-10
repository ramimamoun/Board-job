from django.db import models

# Create your models here.
marital_status = (
    ('Single','Single'),
    ('Married','Married'),
)
class Info(models.Model):
    name = models.CharField(max_length=40)
    picture = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)
    Nationality = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now=True)
    Born_on = models.DateField()
    Marital_Status = models.CharField(max_length=15,choices=marital_status)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(max_length=60)
    address = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    PERSONAL_STATEMENT = models.TextField(max_length=500)
    University = models.CharField(max_length=20,blank=True, null=True)
    specialty = models.CharField(max_length=20,blank=True, null=True)
    grade = models.CharField(max_length=20,blank=True, null=True)
    about_uni = models.TextField(max_length=400,blank=True, null=True)
    course = models.CharField(max_length=30)
    about_course = models.TextField(max_length=400)
    ADDITIONAL_SKILLS = models.CharField(max_length=20)

    def __str__(self):
        return self.name






