from django.db import models
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput, DateInput

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
        widgets = {
            'title': TextInput(attrs={'class': 'span4'}),
            'parole': Textarea(attrs={'class': 'span4', 'rows': 5}),
            'comment': Textarea(attrs={'class': 'span4', 'rows': 5}),
            'author': TextInput(attrs={'class': 'span4'}),
            'source': TextInput(attrs={'class': 'span4'}),
            'date': DateInput(attrs={'class': 'span4'}),
        }
