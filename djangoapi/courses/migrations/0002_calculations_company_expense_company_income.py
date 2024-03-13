# Generated by Django 5.0.2 on 2024-03-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Total_income', models.IntegerField()),
                ('Total_expense', models.IntegerField()),
                ('ProfitorLoss', models.CharField(max_length=10)),
                ('Profit', models.IntegerField()),
                ('Loss', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company_expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Staff', models.IntegerField()),
                ('Rent', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('Otherexpense', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company_income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Grocery', models.IntegerField()),
                ('Bakery', models.IntegerField()),
                ('Clothes', models.IntegerField()),
                ('Electronics', models.IntegerField()),
            ],
        ),
    ]