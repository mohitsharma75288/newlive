# Generated by Django 2.1 on 2018-10-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0003_auto_20181026_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('utype', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
