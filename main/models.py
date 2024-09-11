from django.db import models
from django.core.validators import FileExtensionValidator 




class Subject(models.Model):
    ELEMENTARY = 0
    ADDITIONAL = 1


    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.SmallIntegerField(choices=(
        (ELEMENTARY, "Boshlang'ich"),
        (ADDITIONAL, "Qo'shimcha ")

    ), blank=True, null=True)



    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Maruza"
        verbose_name_plural = "Maruza"




class Practical(models.Model):
    ELEMENTARY = 0
    ADDITIONAL = 1

    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.SmallIntegerField(choices=(
        (ELEMENTARY, "Boshlang'ich"),
        (ADDITIONAL, "Qo'shimcha ")

    ), blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Amaliy mashg'ulot"
        verbose_name_plural = "Amaliy mashg'ulot"








class Independent(models.Model):
    ELEMENTARY = 0
    ADDITIONAL = 1

    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.SmallIntegerField(choices=(
        (ELEMENTARY, "Boshlang'ich"),
        (ADDITIONAL, "Qo'shimcha ")

    ), blank=True, null=True)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Mustaqil ish"
        verbose_name_plural = "Mustaqil ishlar"
    


class Presentation(models.Model):
    ELEMENTARY = 0
    ADDITIONAL = 1

    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.SmallIntegerField(choices=(
        (ELEMENTARY, "Boshlang'ich"),
        (ADDITIONAL, "Qo'shimcha ")

    ), blank=True, null=True)
    def __str__(self):
        return self.name    


    class Meta:
        verbose_name = "Taqdimot"
        verbose_name_plural = "Taqdimotlar"


class Video(models.Model):
    ELEMENTARY = 0
    ADDITIONAL = 1

    video = models.FileField(upload_to='videos_uploaded')
    name = models.CharField(max_length=50, verbose_name="youtube url joylash")
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.SmallIntegerField(choices=(
        (ELEMENTARY, "Boshlang'ich"),
        (ADDITIONAL, "Qo'shimcha ")

    ), blank=True, null=True)

    def __str__(self):
        return self.text   


    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"


  


 
class Pdf(models.Model):
    pdf = models.FileField(upload_to='pdf/')
    name = models.CharField(max_length=250)
    
    
    class Meta:
        verbose_name = "PDF"
        verbose_name_plural = "PDFLar"
    
    def __str__(self):
        return self.name  
    
    
    