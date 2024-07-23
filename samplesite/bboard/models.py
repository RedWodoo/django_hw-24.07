from django.db import models

is_all_posts_passive = True


def is_active_default():
    return is_all_posts_passive


class Roditel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Родители'
        verbose_name = 'Родитель'
        ordering = ['name']


class Rebenok(models.Model):
    KINDS = (
        (None, 'Выберите тип rebenka'),
        ('b', 'Son'),
        ('s', 'Daughter'),
    )

    kind = models.CharField(max_length=1, choices=KINDS, blank=True)

    roditel = models.ForeignKey("Roditel", null=True, on_delete=models.PROTECT,
                                verbose_name='Roditel')
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    title = models.CharField(max_length=50, verbose_name="Rebenok")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Изменено")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Rebenki'
        verbose_name = 'Rebenok'
        ordering = ['-published', 'title']
