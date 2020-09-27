from django.db import models

# Create your models here.

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60,)
    Course_Number = models.IntegerField(max_length=60, default="", blank=True, null=False)
    Instructor_Name = models.TextField(max_length=300, default="", blank=True)
    Duration = models.DecimalField(default=0.00, max_digits=10000,decimal_places=2 )

    objects = models.Manager()

    def __str__(self):
        return self.Title