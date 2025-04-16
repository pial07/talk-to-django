from openai import OpenAI
from decouple import config
from products.models import Product,Embedding
from sentence_transformers import SentenceTransformer
from django.apps import apps
from pgvector.django import CosineDistance
from django.db.models import F

EMBEDDING_MODEL =config("EMBEDDING_MODEL", default="text-embedding-3-small")
EMBEDDING_LENGTH=config("EMBEDDING_LENGTH", default=1536, cast=int)

OPENAI_API_KEY= config("OPENAI_API_KEY")


client = OpenAI(
    api_key=OPENAI_API_KEY
)

def get_embedding(text,model=EMBEDDING_MODEL):
    text=text.replace("\n","").strip()
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def get_query_embedding(text):
    return get_embedding(text) 

def search_posts(query, limit=5):
    BlogPost = apps.get_model(app_label='blog', model_name='BlogPost')
    query_embedding = get_query_embedding(query)
    qs=BlogPost.objects.annotate(distance=CosineDistance('embedding',query_embedding),
                             similarity=1-F("distance")).order_by("distance")[:limit]
    return qs    