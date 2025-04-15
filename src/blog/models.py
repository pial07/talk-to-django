from django.db import models
from pgvector.django import VectorField

import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL= SentenceTransformer("all-MiniLM-L6-v2")
EMBEDDING_LENGTH = 384  # Example dimension size, adjust as needed
# https://platform.openai.com/docs/guides/embeddings
# EMBEDDING_MODEL= "text-embedding-3-small"
# EMBEDDING_LENGTH = 1536  # Example dimension size, adjust as needed

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH,blank=True, null=True)  # Example dimension size, adjust as needed
    can_delete= models.BooleanField(default=False, help_text="Use in Jupyter Notebook")

    def get_embedding_text_raw(self):
        return self.content