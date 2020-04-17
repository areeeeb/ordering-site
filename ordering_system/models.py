from django.db import models


class Pizza(models.Model):
    flavour = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='pizzas')
    large_price = models.FloatField()
    regular_price = models.FloatField()
    small_price = models.FloatField()
    speciality = models.BooleanField(default=False)

    def __str__(self):
        return self.flavour


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    trusted = models.BooleanField(default=False)

    def __str__(self):
        return f'Customer id. {self.id}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField()
    items = models.TextField()
    instructions = models.TextField()
    time = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
