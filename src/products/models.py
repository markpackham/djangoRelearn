from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.FloatField() 
    summary = models.TextField(blank=False, null=False)
    features = models.BooleanField(default=True)

    def get_absolute_url(self):
        # more dynamic than /products/{self.id} since we might change /products/ in the future
        return reverse("product-detail", kwargs={"id": self.id})
