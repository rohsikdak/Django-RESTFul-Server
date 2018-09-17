from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=12)
    email = models.CharField(max_length=40)
    profileImg = models.CharField(max_length=200)
    vec1 = models.FloatField()
    vec2 = models.FloatField()
    vec3 = models.FloatField()
    vec4 = models.FloatField()
    vec5 = models.FloatField()

    def __str__(self):
        return self.nickname


class BasePost(models.Model):
    title = models.CharField(max_length=50)
    contexts = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    vec1 = models.FloatField()
    vec2 = models.FloatField()
    vec3 = models.FloatField()
    vec4 = models.FloatField()
    vec5 = models.FloatField()

    def __str__(self):
        return self.title

class ImagePost(BasePost):
    imgLink = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BasePost, on_delete=models.CASCADE)
    contexts = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.contexts

class LectureBoard(models.Model):
    lec_num = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    professor = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {}".format(self.subject, self.professor)
       