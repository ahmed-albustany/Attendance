# Generated by Django 5.1.2 on 2024-10-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='age_range',
            field=models.CharField(default=(12, 14), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
