# Generated by Django 3.1.6 on 2021-02-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_instrument'),
    ]

    operations = [
        migrations.CreateModel(
            name='assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_id', models.CharField(max_length=50)),
                ('regi_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='instrument',
            name='ins_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
