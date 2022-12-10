from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

class Page(models.Model):
  user = models.CharField(max_length=600)
  pic = models.ImageField(upload_to='images', default='images/default.png')
  bio = models.CharField(max_length=10000)
  watermark = models.BooleanField(default=True)
  views = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.user}'s page"

class Category(models.Model):
  name = models.CharField(max_length=600)
  page = models.ForeignKey(Page, on_delete=models.CASCADE)

  def __str__(self):
    return f"Category {self.name} on page {self.page}"

class Link(models.Model):
  name = models.CharField(max_length=600)
  url = models.CharField(max_length=600)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  page = models.ForeignKey(Page, on_delete=models.CASCADE)

  def __str__(self):
    return f"Link with name {self.name} and url {self.url} on {self.category}"

class Style(models.Model):
  page = models.ForeignKey(Page, on_delete=models.CASCADE)
  css = models.CharField(max_length=1000000)

  def __str__(self):
    return f"Stylesheet {self.css} on {self.page}"
