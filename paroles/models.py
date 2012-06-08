from django.db import models
from django.utils import timezone as tz
from django.forms import ModelForm, Textarea, TextInput, DateInput
from django.template.defaultfilters import slugify

from parole2.settings import PAROLES_PUB_HOUR

def get_pub_date():
    """
        Publication date
        If current hour is after publication hour: return today
        else: return yesterday
    """
    now = tz.localtime(tz.now())
    if now.hour >= PAROLES_PUB_HOUR:
        return now.date()
    else:
        return now.date() - tz.timedelta(1)

class ParoleManager(models.Manager):
    def published(self):
        return super(ParoleManager, self).get_query_set() \
                .filter(date__lte=get_pub_date())

    def not_published(self):
        return super(ParoleManager, self).get_query_set() \
                .filter(date__gt=get_pub_date())

    def last_published(self):
        return super(ParoleManager, self).get_query_set() \
                .filter(date__lte=get_pub_date()) \
                .order_by('date').reverse()[0:1].get()

    def next_published(self, date):
        return super(ParoleManager, self).get_query_set() \
                .filter(date__lte=get_pub_date()) \
                .filter(date__gt=date) \
                .order_by('date')[0:1].get()

    def previous_published(self, date):
        return super(ParoleManager, self).get_query_set() \
                .filter(date__lte=get_pub_date()) \
                .filter(date__lt=date) \
                .order_by('date').reverse()[0:1].get()

class Parole(models.Model):
    title = models.CharField(max_length=255)
    parole = models.TextField()
    comment = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    date = models.DateField(unique=True)
    author_slug = models.SlugField()
    title_slug = models.SlugField()

    objects = ParoleManager()

    def is_published(self):
        return self.date <= get_pub_date()

    def __unicode__(self):
        return self.author + ' - ' + self.title

    def save(self, *args, **kwargs):
        self.author_slug = slugify(self.author)
        self.title_slug = slugify(self.title)
        super(Parole, self).save(*args, **kwargs)

class ParoleForm(ModelForm):
    class Meta:
        model = Parole
        exclude = ('author_slug', 'title_slug',)
        widgets = {
            'title': TextInput(attrs={'class': 'span4'}),
            'parole': Textarea(attrs={'class': 'span4', 'rows': 5}),
            'comment': Textarea(attrs={'class': 'span4', 'rows': 5}),
            'author': TextInput(attrs={'class': 'span4'}),
            'source': TextInput(attrs={'class': 'span4'}),
            'date': DateInput(attrs={'class': 'span4'}),
        }
