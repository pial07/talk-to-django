from django.db import models
from pgvector.django import VectorField

from . import services

EMBEDDING_MODEL= services.EMBEDDING_MODEL
EMBEDDING_LENGTH = services.EMBEDDING_LENGTH


class BlogPost(models.Model):
    title = models.CharField(max_length=200)                                            
    content = models.TextField()
    _content = models.TextField(blank=True, null=True)  # Store the raw content for embedding
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH,blank=True, null=True)  # Example dimension size, adjust as needed
    can_delete= models.BooleanField(default=False, help_text="Use in Jupyter Notebook")
    
    # def save(self, *args, **kwargs):
    #     has_changed = False
    #     if self._content != self.content:
    #         has_changed = True
    #         self._content = self.content
    #     if (self.embedding is None) or has_changed == True:
    #         raw_embedding_text = self.get_embedding_text_raw()
    #         if raw_embedding_text is not None:
    #            self.embedding = services.get_embedding(raw_embedding_text)
    #     super().save(*args, **kwargs)



    def get_embedding_text_raw(self):
        return self.content