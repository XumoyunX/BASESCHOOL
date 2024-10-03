from django.db import models
from django.core.validators import FileExtensionValidator 
from client.models import User



class Subject(models.Model):
    ELEMENTARY = 0
    ADDITIONAL = 1


    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=50)
    text = models.TextField()
    pdf = models.FileField(upload_to='pdf/')
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

    name = models.CharField(max_length=50, verbose_name="youtube url joylash")
    text = models.TextField(verbose_name="Nima haqida")
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


  


 
    
    
    
    



class Test(models.Model):
    title = models.CharField(max_length=200, verbose_name="Test Yo'nalish")
    duration = models.DurationField(verbose_name="Vaqti")  # Test davomiyligi
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Test yo'nalishi"
        verbose_name_plural = "Test yo'nalishi"


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="Savol yozing")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    
    class Meta:
        verbose_name = "Test Savol"
        verbose_name_plural = "Test Savol"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(verbose_name="Javob yozing")
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri javobmi?")  # To'g'ri javobmi?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} - {self.question}"

    class Meta:
        verbose_name = "Test Javobi"
        verbose_name_plural = "Test Javobi"

class UserTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tests')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='user_tests')
    score = models.IntegerField(default=0, verbose_name="Foydalanuvchining balli")  # Foydalanuvchining balli
    completed_at = models.DateTimeField(auto_now_add=True)  # Testni tugatgan vaqti

    class Meta:
        unique_together = ('user', 'test')  # Har bir foydalanuvchi uchun test yagona bo'lishi kerak

    def __str__(self):
        return f"{self.user.username} - {self.test.title}"
    
    
    
    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natija"