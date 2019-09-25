# Generated by Django 2.2.2 on 2019-09-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20190922_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratorReadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genstatementID', models.CharField(max_length=10, unique=True)),
                ('consumerID', models.CharField(blank=True, max_length=12)),
                ('statementMonth', models.CharField(blank=True, max_length=2)),
                ('statementYear', models.CharField(blank=True, max_length=4)),
                ('companyName', models.CharField(blank=True, max_length=150)),
                ('impUnitsC1', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('impUnitsC2', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('impUnitsC3', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('impUnitsC4', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('impUnitsC5', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('expUnitsC1', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('expUnitsC2', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('expUnitsC3', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('expUnitsC4', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('expUnitsC5', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('netUnitsC1', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('netUnitsC2', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('netUnitsC3', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('netUnitsC4', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('netUnitsC5', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('bankingC1', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('bankingC2', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('bankingC3', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('bankingC4', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('bankingC5', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC002', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC003', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC004', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC005', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC006', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC007', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('chargesC001', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
            ],
        ),
    ]