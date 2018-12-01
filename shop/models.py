from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.core.urlresolvers import reverse

# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}


# Модель категории
class Category( models.Model ):
    name = models.CharField( max_length=200, db_index=True, verbose_name='Имя' )
    slug = models.SlugField( max_length=200, db_index=True, unique=True )

    def get_absolute_url(self):
        return reverse( 'shop:ProductListByCategory', args=[self.slug] )

# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d/', verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def get_absolute_url(self):
        return reverse( 'shop:ProductDetail', args=[self.id, self.slug])

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

