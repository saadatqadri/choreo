from django.db import models
from manageconfig.models import ConfigurationItem

STATUS_CHOICES = (
    ('PLANNED', 'Planned'),
    ('APPROVED', 'Approved'),
    ('DEFERRED', 'Deferred'),
    ('CANCELLED', 'Cancelled'),
    ('SUCCESS', 'Success'),
    ('FAILURE', 'Failure'),
    ('REJECTED', 'Rejected'),
    ('UNDER_REVIEW', 'Under Review'),
    ('DOCUMENTATION_APPROVED', 'Documentation Approved'),
    ('INITIAL_APPROVAL', 'Initial Approval'),
    ('FINAL_APPROVAL', 'Final Approval'),
    ('INFORMATION_ONLY', 'Information Only'),
    ('CLOSED', 'Closed'),
)

TYPE_CHOICES = (
    ('ADD', 'Add'),
    ('CHANGE', 'Change'),
    ('REMOVE', 'Remove'),
)

IMPACT_CHOICES = (
    ('HIGH', 'High'),
    ('MED', 'Medium'),
    ('LOW', 'Low'),
)

URGENCY_CHOICES = (
    ('HIGH', 'High'),
    ('MED', 'Medium'),
    ('LOW', 'Low'),
)
# Create your models here.

class ChangeRequest(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    nomsv2 = models.CharField(max_length=12, blank=True)
    configitem = models.ForeignKey(ConfigurationItem)
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    reason = models.TextField()
    description = models.TextField()
    change_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    impact = models.CharField(max_length=20, choices=IMPACT_CHOICES)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    details = models.TextField()
    testing = models.TextField()
    impact_details = models.TextField()
    backout = models.TextField()
    change_artifacts = models.TextField()
    initial_approver = models.CharField(max_length=255)
    final_approver = models.CharField(max_length=255)
    implementor = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)

