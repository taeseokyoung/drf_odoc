from django.db import models

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,
                             verbose_name="작성자", related_name="articles")
    title = models.CharField("제목", max_length=100)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(
        "articles.Article", on_delete=models.CASCADE, verbose_name="게시글", related_name="comments")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,
                             verbose_name="작성자", related_name="comments")
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
