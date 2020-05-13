from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def clean(self):
        self.name = self.name.title()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    is_indian = models.BooleanField(default=False)

    class Meta:
        unique_together = (('name', 'category'))

    def clean(self):
        self.name = self.name.title()

    def __str__(self):
        return self.name

    