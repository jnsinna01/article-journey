from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, UserViewSet

#from .views import ApiListCreateArticle, ApiEditDeleteArticle, ApiEditDeleteUser, ApiListCreateUser
#from django.urls import path

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', ArticleViewSet, basename='articles')
urlpatterns = router.urls

#urlpatterns = [
    #path('users/<int:pk>/', ApiEditDeleteUser.as_view()),
    #path('users/', ApiListCreateUser.as_view()),
    #path('<int:pk>/', ApiEditDeleteArticle.as_view()),
    #path('', ApiListCreateArticle.as_view()),
#]