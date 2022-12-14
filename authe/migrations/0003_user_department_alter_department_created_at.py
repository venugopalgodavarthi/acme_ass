# Generated by Django 4.1.2 on 2022-10-31 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0002_remove_user_created_at_remove_user_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authe.department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
