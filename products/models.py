from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menu"


class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"


class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    nutrition = models.ForeignKey("Nutrition", on_delete=models.CASCADE)
    allergy = models.ManyToManyField("Allergy", through="AllergyProduct")

    class Meta:
        db_table = "products"


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "images"


class Nutrition(models.Model):
    kcal = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sodium = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sugar = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    caffeine = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        db_table = "nutritions"


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergies"


class AllergyProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "allergies_products"
