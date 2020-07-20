# Generated by Django 3.0.7 on 2020-06-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200625_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_jason', models.CharField(default='', max_length=3000)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
