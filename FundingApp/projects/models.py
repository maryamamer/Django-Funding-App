from django.db import models
from django.contrib.auth.models import User
from users.models import user
from datetime import datetime
from django.urls import  reverse


# Create model gor booktype


class Categories(models.Model):
    categoryTitle = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.categoryTitle

class Project(models.Model):
    user = models.ForeignKey('users.user', null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=20)
    details = models.TextField('Details')
    category = models.ForeignKey(
        'Categories', null=True, on_delete=models.CASCADE)
    totalTarget = models.IntegerField()
    startproject = models.DateField("Start Date")
    endproject = models.DateField("End Date")


class Images (models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media/projects/img")

class Comment (models.Model):
    comment_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey('projects.Project', related_name="comments", on_delete=models.CASCADE)
    comment_content = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment_content)


class Donation (models.Model):
    donation_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey('projects.Project', related_name="donations", on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.user', on_delete=models.CASCADE)
    donation_amount = models.IntegerField()

    def __str__(self):
        return f"{self.user_id} - {self.project_id}"


class Rating (models.Model):
    rating_id = models.AutoField(primary_key=True)
    Rating_project_id = models.ForeignKey('projects.Project', related_name="Rating", on_delete=models.CASCADE)
    rate_content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Rate {}'.format(self.rate_content)
