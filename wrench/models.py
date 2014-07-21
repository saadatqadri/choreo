from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('project-view', kwargs={'pk': self.id})

    def __unicode__(self):
        return self.name


class Plan(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def get_absolute_url(self):
        return reverse('plan-view', kwargs={'pk_proj': self.project.id, 'pk': self.id})

    def __unicode__(self):
        return self.name


class Suite(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('suite-view', kwargs={'pk_proj': self.project.id, 'pk': self.id})

    def __unicode__(self):
        return self.name


CASE_STATUS_CHOICES = (
    ('NO_RUN', 'No Run'),
    ('PASS', 'Passed'),
    ('FAIL', 'Failed'),
    ('SKIP', 'Skipped'),
)

class Case(models.Model):
    suite = models.ForeignKey(Suite)
    title = models.CharField(max_length=255)
    description = models.TextField()
    procedure = models.TextField()
    expected = models.TextField()
    notes = models.TextField()
    clean_up = models.TextField()
    status = models.CharField(choices=CASE_STATUS_CHOICES, default='NO_RUN', max_length=24)

    def get_absolute_url(self):
        return reverse('case-view', kwargs={'pk_proj': self.suite.project.id,
                                            'pk_suite': self.suite.id,
                                            'pk': self.id
                                            })

    def __unicode__(self):
        return self.title

class Run(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    assigned_to = models.CharField(max_length=255)  # user

    def __unicode__(self):
        return self.name
