# Generated by Django 5.1.1 on 2024-09-28 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0020_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Event.vendor'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(choices=[('caterer', 'Caterer'), ('florist', 'Florist'), ('dj', 'DJ'), ('photographer', 'Photographer'), ('decorator', 'Decorator'), ('other', 'Other')], max_length=50),
        ),
    ]
