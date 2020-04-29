from django.db import models

# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=30)
    weight=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    created_at=models.DateField(auto_now_add=False)
    updated_at=models.DateField(auto_now_add=False)

    class Meta:
        # app_label = 'product_db'
        managed = True
        db_table = 'pr_details'

    def __str__(self):
        return self.name
