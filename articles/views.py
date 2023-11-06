from .models import Post, Tag
from .serializers import PostSerializers, TagSerializers
from rest_framework import viewsets
from rest_framework.mixins import DestroyModelMixin


from rest_framework.authentication import SessionAuthentication
from blogDjnago.utils import IsAuthenticatedForPostOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedForPostOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedForPostOnly]
