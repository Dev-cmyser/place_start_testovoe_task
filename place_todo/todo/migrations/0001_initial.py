# Generated by Django 4.2 on 2023-04-16 12:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_to', models.DateTimeField(blank=True, null=True)),
                ('updated_to', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('hight', 'hight'), ('medium', 'medium'), ('low', 'low')], default='low', max_length=6)),
                ('status', models.CharField(choices=[('in progress', 'in progress'), ('done', 'done'), ('pending', 'pending')], default='pending', max_length=30)),
                ('title', models.CharField(max_length=90)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
