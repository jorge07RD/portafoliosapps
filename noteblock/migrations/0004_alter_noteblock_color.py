# Generated by Django 3.2.5 on 2021-08-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteblock', '0003_alter_noteblock_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteblock',
            name='color',
            field=models.CharField(choices=[('0', 'dark'), ('1', 'success'), ('2', 'info'), ('3', 'warning'), ('4', 'danger')], max_length=11),
        ),
    ]
