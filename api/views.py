from rest_framework import viewsets, generics
from articles.models import Article
from users.models import CustomUser
from .serializers import ArticleSerializer, CustomUserSerializer
#from .permissions import IsAuthorOrReadOnly
#from rest_framework import permissions


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (IsAuthorOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    #permission_classes = (permissions.IsAuthenticated,)


#class ApiListCreateArticle(generics.ListCreateAPIView):
    #queryset = Article.objects.all()
    #serializer_class = ArticleSerializer


#class ApiEditDeleteArticle(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Article.objects.all()
    #serializer_class = ArticleSerializer


#class ApiEditDeleteUser(generics.RetrieveUpdateDestroyAPIView):
    #queryset = CustomUser.objects.all()
    #serializer_class = CustomUserSerializer


#class ApiListCreateUser(generics.ListCreateAPIView):
    #queryset = CustomUser.objects.all()
    #serializer_class = CustomUserSerializer
