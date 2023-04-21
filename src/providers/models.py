from django.db import models

class Provider(models.Model):
    # The original id from the json file - kept for reference but not recommended for actual use
    id = models.IntegerField()
    # Unique id with auto increment
    id_uuid = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=30)
    birth_date = models.DateField()
    rating = models.FloatField()
    primary_skills = models.JSONField()
    secondary_skill = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    active = models.BooleanField()
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    class Meta:
        # Sort the results by rating
        ordering = ['-rating']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
