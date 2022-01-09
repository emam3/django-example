from django.db import models

# Create your models here.

class Instructor():
    id = models.Field(primary_key = True)
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    rate = models.FloatField(min_value=0.0, max_value=5.0)
    description = models.CharField(max_length=2500)


class Category():
    id = models.Field(primary_key = True)
    name = models.CharField(max_length=250)


class Course():
    id = models.Field(primary_key = True)
    name = models.CharField(max_length=250)
    details = models.CharField(max_length=2500)
    price = models.IntgerField()
    language = models.CharField(max_length=250)
    category_id = models.ForeignKey(Category.id)
    instructor_id = models.ForeignKey(Instructor.id)
    instructor = models.ManyToManyField(Instructor)


class Courses_Images_videos_Texts():
    id = models.Field(primary_key = True)
    type = models.CharField(max_length=2500)
    course_id = models.ForeignKey(Course.id)