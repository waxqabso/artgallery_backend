# Generated by Django 2.2.1 on 2019-05-03 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_auto_20190503_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='artist_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='art.Artist'),
        ),
    ]
