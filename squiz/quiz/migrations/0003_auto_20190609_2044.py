# Generated by Django 2.2.2 on 2019-06-09 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='correct_ans',
            new_name='selected_option',
        ),
    ]
