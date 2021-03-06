# Generated by Django 2.2.4 on 2019-11-30 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_remove_household_authentication_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiverecord',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='有效日期'),
        ),
        migrations.AddField(
            model_name='sendrecord',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='有效日期'),
        ),
        migrations.AlterField(
            model_name='contacter',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名稱'),
        ),
    ]
