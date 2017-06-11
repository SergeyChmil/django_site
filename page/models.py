from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Good(models.Model):
    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "price", "name")
        verbose_name = 'good'
        verbose_name_plural = 'goods'

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    description = models.TextField()
    price = models.FloatField()
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='In stock')
    category = models.ForeignKey(Category)

    def get_in_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s += " (not in stock)"
        return s


class BlogArticle(models.Model):
    title = models.CharField(max_length=30, unique_for_date='pubdate')
    pubdate = models.DateField()
    updated = models.DateTimeField(auto_now=True)
