from django.db import models

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=30,default="")
    category= models.CharField(max_length=30, default="")
    desc = models.CharField(max_length=500, default="")
    price=models.IntegerField(default=0)
    pub_date= models.DateField()
    image=models.ImageField(upload_to='shop/media',default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="")
    email= models.CharField(max_length=30, default="")
    query = models.CharField(max_length=500, default="")
    phone=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=3000,default="")
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=30,default="")
    email= models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=10, default="")
    address=models.CharField(max_length=500, default="")
    city=models.CharField(max_length=50, default="")
    state=models.CharField(max_length=50, default="")
    zip_code=models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=500, default="")
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:10] + "..."

