# Generated by Django 4.2.5 on 2024-12-14 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theories', '0002_theoryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theoryimage',
            name='image',
            field=models.ImageField(upload_to='theory_website/media'),
        ),
        migrations.AlterField(
            model_name='theoryimage',
            name='theory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theories_images', to='theories.theory'),
        ),
    ]
