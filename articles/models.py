from django.db import models
from django.urls import reverse
from users.models import CustomUser
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='articles_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    @staticmethod
    def get_absolute_url():
        return reverse('article_list')
