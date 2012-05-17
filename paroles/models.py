from django.db import models

class Parole(models.Model):
    title = models.CharField(max_length=255)
    parole = models.TextField()
    comment = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    date = models.DateField(unique=True)

    def __unicode__(self):
        return self.author + ' - ' + self.title
