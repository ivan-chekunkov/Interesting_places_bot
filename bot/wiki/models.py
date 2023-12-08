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
        return (
            self.main_district.name[:10]
            + "-"
            + self.neighboring_district.name[:10]
        )


class Picture(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Дата создания записи",
        auto_now_add=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование изображения",
        help_text="Введите название изображения",
    )
    image = models.ImageField(
        upload_to="",
        verbose_name="Путь до файла изображения",
        help_text="Укажите путь до файла изображения",
    )
    location = models.ForeignKey(
        to="Location",
        on_delete=models.CASCADE,
        verbose_name="Локация",
        blank=True,
        null=True,
        related_name="picture",
    )

    class Meta:
        db_table = "pictures"
        db_table_comment = "Table of pictures"
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name[:10]


class Category(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Дата создания записи",
        auto_now_add=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите название категории",
    )

    class Meta:
        db_table = "categoryes"
        db_table_comment = "Table of categoryes"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name[:10]


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
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Категория",
    )
    district = models.ForeignKey(
        to=District,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Район",
    )

    class Meta:
        db_table = "locations"
        db_table_comment = "Table of interesting places"
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name[:10]
