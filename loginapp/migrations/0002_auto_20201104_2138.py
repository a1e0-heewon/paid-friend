# Generated by Django 3.1.3 on 2020-11-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='asdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('school', models.TextField()),
                ('gender', models.TextField()),
                ('birth', models.TextField()),
                ('hobby', models.TextField()),
                ('mbti', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]