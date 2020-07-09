from django.db import models
from datetime import datetime, date
from django.core.urlresolvers import reverse

# Create your models here.

class Appointment(models.Model):
    #patient = models.ForeignKey(Patient)
    #doctor = models.ForeignKey(Doctor)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def has_passed(self):
        return self.end_time < datetime.now()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('appointment-detail', kwargs={"pk":self.pk})

