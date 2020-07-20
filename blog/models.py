from django.db import models

# Create your models here.

class BlogPost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    head0= models.CharField(max_length=90, default="")
    chead0= models.CharField(max_length=300, default="")
    head1= models.CharField(max_length=90, default="")
    chead1= models.CharField(max_length=300, default="")
    head2= models.CharField(max_length=90, default="") 
    chead2= models.CharField(max_length=300, default="") 
    pub_date= models.DateField()
    image=models.ImageField(upload_to='blog/media',default="")

    def __str__(self):
        return self.title
