from django.db import models


class District(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Дата создания записи",
        auto_now_add=True,
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование района",
        help_text="Введите название района",
    )
    adjacent_district = models.ManyToManyField(
        to="self",
        through="Adjacent_district",
        related_name="district",
        blank=True,
    )

    class Meta:
        db_table = "districts"
        db_table_comment = "Table of city districts"
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        ordering = ["-date_created"]

    def __str__(self) -> str:
        return self.name[:10]


class Adjacent_district(models.Model):
    main_district = models.ForeignKey(
        to=District,
        on_delete=models.CASCADE,
        related_name="main_district",
        blank=True,
    )
    neighboring_district = models.ForeignKey(
        to=District,
        on_delete=models.CASCADE,
        related_name="neighboring_district",
        blank=True,
    )

    class Meta:
        db_table = "adjacent_districts"
        db_table_comment = "Table of adjacent areas"
        verbose_name = "Соседний район"
        verbose_name_plural = "Соседние районы"
        ordering = ["main_district", "neighboring_district"]

    def __str__(self) -> str:
        return self.main_district[:10] + " " + self.neighboring_district[:10]


class Picture(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование изображения",
        help_text="Введите название изображения",
    )


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
