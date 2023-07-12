# Generated by Django 4.2.3 on 2023-07-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
