# Generated by Django 3.2.9 on 2021-11-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=30)),
                ('To', models.CharField(max_length=30)),
                ('Price', models.IntegerField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
