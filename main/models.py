from django.db import models
from django.core.validators import FileExtensionValidator 




class Subject(models.Model):
    ELEMENTARY = "E"
    ADDITIONAL = "A"
    ACCOUNT_TYPE_CHOICES = {
        ELEMENTARY: "Boshlang'ich ",
        ADDITIONAL: "Qo'shimcha ",

    }
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=ELEMENTARY,
    )

    def __str__(self):
        return self.name




class Practical(models.Model):
    ELEMENTARY = "E"
    ADDITIONAL = "A"
    ACCOUNT_TYPE_CHOICES = {
        ELEMENTARY: "Boshlang'ich ",
        ADDITIONAL: "Qo'shimcha ",

    }
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=ELEMENTARY,
    )

    def __str__(self):
        return self.name








class Independent(models.Model):
    ELEMENTARY = "E"
    ADDITIONAL = "A"
    ACCOUNT_TYPE_CHOICES = {
        ELEMENTARY: "Boshlang'ich ",
        ADDITIONAL: "Qo'shimcha ",

    }
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=ELEMENTARY,
    )

    def __str__(self):
        return self.name
    


class Presentation(models.Model):
    ELEMENTARY = "E"
    ADDITIONAL = "A"
    ACCOUNT_TYPE_CHOICES = {
        ELEMENTARY: "Boshlang'ich ",
        ADDITIONAL: "Qo'shimcha ",

    }
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=ELEMENTARY,
    )

    def __str__(self):
        return self.name    



class Video(models.Model):
    ELEMENTARY = "E"
    ADDITIONAL = "A"
    ACCOUNT_TYPE_CHOICES = {
        ELEMENTARY: "Boshlang'ich ",
        ADDITIONAL: "Qo'shimcha ",

    }
    video = models.FileField(upload_to='videos_uploaded')
    name = models.CharField(max_length=50)
    text = models.TextField()
    registered_on = models.DateField(auto_now_add=True)

    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=ELEMENTARY,
    )

    def __str__(self):
        return self.name   



  
