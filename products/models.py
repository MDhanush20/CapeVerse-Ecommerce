from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='categories/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()

    trending = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name