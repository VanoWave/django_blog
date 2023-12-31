from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=155, verbose_name="Название категорий")


    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок статьи", max_length=155, unique=True)
    short_description = models.TextField(verbose_name="Краткое описание", max_length=300)
    full_description = models.TextField(verbose_name="Полное описание,")
    photo = models.ImageField(verbose_name="Фото", upload_to="photos/articles/")
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата обновления",auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="articles")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="articles")