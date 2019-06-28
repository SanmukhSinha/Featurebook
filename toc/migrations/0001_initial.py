# Generated by Django 2.2.2 on 2019-06-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
                ('text', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Heading',
                'verbose_name_plural': 'Headings',
            },
        ),
    ]