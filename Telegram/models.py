from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=50)
    api_id = models.CharField(max_length=50)
    api_hash = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Member(models.Model):
    chat_id = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.chat_id)
