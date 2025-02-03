from django.db import models

# Create your models here.
class About(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    short_bio = models.CharField(max_length=300)
    location = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    specialties = models.TextField(help_text="Comma-separated skills (e.g. Python, Django, JavaScript)")
    education = models.TextField()
    work_experience = models.TextField()
    programming_languages = models.TextField()
    frameworks = models.TextField()
    tools = models.TextField()
    services = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name

