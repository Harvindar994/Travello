# Generated by Django 3.2.4 on 2021-06-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
