from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)


class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    occupation = models.CharField(max_length=150)
=======
    occupation = models.CharField(max_length=150)
>>>>>>> 5de256335b71085e60b654c22e944ea7265e2d7e
