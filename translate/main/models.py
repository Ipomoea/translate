from django.db import models


class Entry(models.Model):
    origin = models.CharField(max_length=64)
    date_added = models.DateField(auto_now=True)
    lang_key = models.CharField(max_length=8)


class Subject(models.Model):
    value = models.CharField(max_length=64)
    lang_code = models.CharField(max_length=4)


class Translate(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT)
    value = models.CharField(max_length=64)
