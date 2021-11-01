from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    chat_id = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Member(models.Model):
    user_id = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.user_id)
