from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('project-view', kwargs={'pk': self.id})


class Plan(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project)


class Suite(models.Model):
    name = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan)


class Case(models.Model):
    suite = models.ForeignKey(Suite)
    title = models.CharField(max_length=255)
    description = models.TextField()
    procedure = models.TextField()
    expected = models.TextField()


class Run(models.Model):
    name = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan)
    assigned_to = models.CharField(max_length=255)  # user
