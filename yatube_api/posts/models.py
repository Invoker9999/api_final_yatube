from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import (
    MAXIMUM_STRING_LENGTH,
    NUMBER_OF_VISIBLE_CHARACTERS
)

User = get_user_model()


class Group(models.Model):
    """Группа."""
    title = models.CharField(
        max_length=MAXIMUM_STRING_LENGTH,
        verbose_name='Оглавление группы'
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание группы')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('slug',)

    def __str__(self):
        return self.title[:NUMBER_OF_VISIBLE_CHARACTERS]


class Post(models.Model):
    """Публикация."""
    text = models.TextField(verbose_name='Тескт публикации')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка публикации')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа публикации'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = (
            'group',
            'pub_date',
            'author__username',
        )

    def __str__(self):
        return self.text[:NUMBER_OF_VISIBLE_CHARACTERS]


class Comment(models.Model):
    """Комментарий."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация комментария'
    )
    text = models.TextField(verbose_name='Текст комметария')
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return self.text[:NUMBER_OF_VISIBLE_CHARACTERS]


class Follow(models.Model):
    """Подписка."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписан'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_subscriber_author_pair'
            )
        ]
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('user',)

    def __str__(self):
        return f'follower:{self.user}, following:{self.following}'
