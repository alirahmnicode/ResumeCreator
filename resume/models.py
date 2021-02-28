from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    marital_CHOICES = (
        ("single", "single"),
        ("rel", "rel"),
    )
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(
        max_length=150, choices=marital_CHOICES, blank=True, null=True
    )
    image = models.ImageField(blank=True)
    job = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=150, blank=True)
    phon = models.CharField(max_length=150, blank=True)
    github = models.URLField(max_length=200, blank=True)
    linkdin = models.URLField(max_length=200, blank=True)
    Introduction = RichTextField(blank=True , null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
             url = ''
        return url
        
    def __str__(self):
        return f"{self.first_name , self.last_name , self.age , self.marital_status}"


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class Skills(models.Model):
    skill_name = models.CharField(max_length=150, blank=True)
    skill_level = models.IntegerField(blank=True, null=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name


class Work_Experience(models.Model):
    job = models.CharField(max_length=150, blank=True)
    place = models.CharField(blank=True, null=True, max_length=150)
    description = RichTextField(blank=True , null=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.job


class Education(models.Model):
    university = models.CharField(max_length=150)
    education_level = models.CharField(max_length=150)
    description = RichTextField(blank=True , null=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

