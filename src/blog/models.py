from django.db import models
from pgvector.django import VectorField


# https://platform.openai.com/docs/guides/embeddings
EMBEDDING_MODEL= "text-embedding-3-small"
EMBEDDING_LENGTH = 1536  # Example dimension size, adjust as needed

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH,blank=True, null=True)  # Example dimension size, adjust as needed
