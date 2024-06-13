# Generated by Django 5.0.6 on 2024-05-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_subject_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('registered_on', models.DateField(auto_now_add=True)),
                ('account_type', models.CharField(choices=[('E', "Boshlang'ich "), ('A', "Qo'shimcha ")], default='E', max_length=1)),
            ],
        ),
    ]
