# Generated by Django 2.2.7 on 2022-04-26 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parament_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_tag', to='quiz.Tag'),
        ),
    ]
