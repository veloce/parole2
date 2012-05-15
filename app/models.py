from django.db import models

class Parole(models.Model):
    title = models.CharField(max_length=255)
    parole = models.TextField()
    comment = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return self.author + ' ' + self.title
