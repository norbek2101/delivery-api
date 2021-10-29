from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'  

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Order(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    phone = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    definition = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    STATUS = [
        ('in order', 'in order'),
        ('confirmed', 'confirmed'),
        ('food completed', 'food completed'),
        ('in way', 'in way'),
        ('order completed', 'order completed')
    ]
    status = models.CharField(max_length=200, choices=(STATUS), default='in order')

    def __str__(self):
        return self.name

