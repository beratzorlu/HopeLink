from django.db import models


class Ngo(models.Model):
    """
    modle for ngo page
    """

    name = models.CharField(max_length=250, null=False, default='Add Blog title here', unique=True)
    description = models.TextField(null=False, default='Add Blog content here')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.title
