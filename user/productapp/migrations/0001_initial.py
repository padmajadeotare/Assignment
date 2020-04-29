# Generated by Django 3.0.5 on 2020-04-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
            options={
                'db_table': 'prod_details',
                'managed': True,
            },
        ),
    ]
