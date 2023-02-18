from django.db import models


class Blog(models.Model):
    """
    modle for blog page
    """

    title = models.CharField(max_length=250, null=False, default='Add Blog title here', unique=True)
    body = models.TextField(null=False, default='Add Blog content here')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.title
