from django.db import models
from django.urls import reverse

class Project(models.Model):
    class Status(models.TextChoices):
        SUCCESS = 'Success'
        FAILURE = 'Failure'
        BUILDING = 'Building'
        WAITING = 'Waiting'
        PAUSED = 'Paused'
        UNKNOWN = 'Unknown'

    class SVGPath(models.TextChoices):
        PRODUCT = '<path d="M2 16.1A5 5 0 0 1 5.9 20M2 12.05A9 9 0 0 1 9.95 20M2 8V6a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-6"></path><line x1="2" y1="20" x2="2.01" y2="20"></line>'
        UNIX = '<rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line>'
        CLIENTS = '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>'
        Miroservice = '<rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line>'

    name = models.CharField(max_length=25)
    git_url = models.URLField()
    server_ip = models.CharField(max_length=100, default="127.0.0.1")
    project_slug = models.SlugField(max_length=25, null=False, unique=True)
    svg_path  = models.TextField(choices=SVGPath.choices, default=SVGPath.UNIX)
    version = models.CharField(max_length=25)
    branch = models.CharField(max_length=100)
    status = models.CharField(max_length=25, choices=Status.choices, default=Status.UNKNOWN)
    note = models.CharField(max_length=100, null=True)
    started = models.DateTimeField()
    ended = models.DateTimeField()
    duration = models.DurationField(null=True)

    class Meta:
        # Sort the results by started field in decending order
        ordering = ['-started']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("build_detail", kwargs={"project_slug": self.project_slug})

class BuildData(models.Model):
    class Status(models.TextChoices):
        SUCCESS = 'Success'
        FAILURE = 'Failure'
        BUILDING = 'Building'
        WAITING = 'Waiting'
        PAUSED = 'Paused'
        UNKNOWN = 'Unknown'

    project_slug = models.SlugField(max_length=25, null=False)
    url = models.URLField()
    server_ip = models.CharField(max_length=100, default="127.0.0.1")
    version = models.CharField(max_length=25)
    branch = models.CharField(max_length=100)
    status = models.CharField(max_length=25, choices=Status.choices, default=Status.UNKNOWN)
    note = models.CharField(max_length=100, null=True)
    started = models.DateTimeField()
    ended = models.DateTimeField()
    duration = models.DurationField(null=True)

    class Meta:
        # Sort the results by started field in decending order
        ordering = ['-started']

    def __str__(self):
        return self.project_slug + ": version " + self.version + " on " + self.branch

    def get_absolute_url(self):
        return reverse("build_detail", kwargs={"project_slug": self.project_slug})
