from django.db import models

# Create your models here.
class Job(models.Model):
    employer_name = models.CharField(max_length=255)
    employer_logo = models.CharField(max_length=1000, null=True)
    job_publisher = models.CharField(max_length=255, null=True)
    job_id = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    job_employment_type = models.CharField(max_length=255, null=True)
    job_apply_link = models.CharField(max_length=255, null=True)
    job_description = models.TextField(null=True)
    job_city = models.CharField(max_length=255, null=True)
    job_state = models.CharField(max_length=255, null=True)
    job_country = models.CharField(max_length=255, null=True)
    job_google_link = models.CharField(max_length=1000, null=True)
    job_highlights = models.JSONField(null=True)

    def __str__(self):
        return self.job_title