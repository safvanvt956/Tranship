from django.db import models

# Create your models here.

class Emails(models.Model):

    Email= models.EmailField(max_length=100)

    def __str__(self):
        return self.Email
    
    


class Contact(models.Model):

    Name= models.CharField(max_length=100)
    Email= models.EmailField(max_length=100)
    Phone= models.CharField(max_length=100)
    Service= models.CharField(max_length=100)
    Message= models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    


class Quote(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    Services=models.CharField(max_length=50)
    Best=models.CharField(max_length=50)
    Hear=models.CharField(max_length=50)
    messages=models.TextField()
    

    def __str__(self):
        return self.name
    







class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name  



class Search(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    cate=models.ManyToManyField(Tag)
    author = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="posts")
    publish_timestamp=models.DateTimeField( auto_now_add=False,blank=True,null=True)


 
    def _str_(self):
        return self.title
    

class Search2(models.Model):
    image=models.ImageField()
    title=models.TextField()
    
    def __str__(self):
        return self.title








    




    
    
    


    








    

    







