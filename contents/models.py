from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()    #max_length=1000)
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            GinIndex(fields=["search_vector"]),
        ]
