from django.db import models


# Create your models here.

class user_form(models.Model):
    sex_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    email = models.CharField(max_length=100, default=None)
    instagram_id = models.CharField(max_length=100, default=None)
    sex = models.CharField(max_length=1, choices=sex_choices, blank=True, default=None)
    submission_date = models.DateTimeField(default=None)
    birthday = models.DateTimeField(default=None)
    followers = models.IntegerField(default=None)

    def __str__(self):
        return self.email
        return self.instagram_id
        return self.sex
        return self.birthday  # need this to display data when Quering db
        return self.followers


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
