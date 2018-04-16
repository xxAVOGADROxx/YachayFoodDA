from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=False)
    def get_absolute_url(self):
            return reverse('products:product_list_by_category',
                        args=[self.slug])



    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey( Category ,related_name = 'products')#
    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    limit_date = models.DateTimeField(blank=True, null=True)
    register_date = models.DateField(blank=True, null=True)
    available = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse('products:product_detail',
                        args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        managed = True
        index_together = (('id', 'slug'),)
        db_table = 'product'

    def __str__(self):
        return self.name
