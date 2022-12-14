# Generated by Django 4.1.4 on 2022-12-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя студента')),
                ('surname', models.CharField(max_length=150, verbose_name='фамилия студента')),
                ('gender', models.CharField(choices=[('M', 'M'), ('W', 'W')], max_length=1)),
                ('is_frozen', models.BooleanField(default=False)),
            ],
        ),
    ]
