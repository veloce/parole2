from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class ParoleManager(models.Manager):
    def published(self):
        return super(ParoleManager, self).get_query_set().filter(date__lte=timezone.now())

    def not_published(self):
        return super(ParoleManager, self).get_query_set().filter(date__gt=timezone.now())

class Parole(models.Model):
    title = models.CharField(max_length=255)
    parole = models.TextField()
    comment = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    date = models.DateField(unique=True)

    objects = ParoleManager()

    def is_published(self):
        return self.date <= timezone.now().date()

    def __unicode__(self):
        return self.author + ' - ' + self.title

class ParoleForm(ModelForm):
    class Meta:
        model = Parole
