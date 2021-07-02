from django.db import models

STATUS = (
    ('1', 'Open'),
    ('2', 'To Do'),
    ('3', 'Doing'),
)


class Todo(models.Model):
    text = models.TextField(verbose_name="Text")
    status = models.CharField(max_length=255, verbose_name="Status", choices=STATUS)

    def __str__(self):
        return self.text
