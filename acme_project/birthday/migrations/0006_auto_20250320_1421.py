# Generated by Django 3.2.16 on 2025-03-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_congratulation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
        migrations.AddField(
            model_name='birthday',
            name='tegs',
            field=models.ManyToManyField(blank=True, help_text='Удерживайте CTRL для выбора несколькх вариантов.', to='birthday.Tag', verbose_name='Тэги'),
        ),
    ]
