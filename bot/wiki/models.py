from django.db import models


class Location(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Дата создания записи",
        auto_now_add=True,
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование локации",
        help_text="Введите название локации",
    )
    description = models.CharField(
        max_length=5000,
        verbose_name="Описание локации",
        help_text="Введите описание локации",
    )

    class Meta:
        db_table = "locations"
        db_table_comment = "Table of interesting places"
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name[:10]
