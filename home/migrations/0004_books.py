# Generated by Django 2.1 on 2018-10-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_subuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('adestionation', models.CharField(max_length=200)),
                ('bdestination', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(verbose_name='date and time of reservations')),
            ],
        ),
    ]
