from django.db import models


class Participant(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    favorite_book = models.TextField()

    def __str__(self):
        return self.name


class FormModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FormField(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FormData(models.Model):
    objects = models.Manager()
    form_id = models.IntegerField()
    field_id = models.IntegerField()
    value = models.CharField(max_length=50)
    record_id = models.IntegerField()

    def __str__(self):
        return f"form_id: {self.form_id}, " \
               f"field_id: {self.field_id}, " \
               f"record_id: {self.record_id}"


class FormRecord(models.Model):
    objects = models.Manager()
    date = models.DateTimeField()

    def __str__(self):
        return self.date
