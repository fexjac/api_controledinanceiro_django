# Generated by Django 4.1.7 on 2023-03-29 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_rename_user_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=10)),
                ('saldo_banco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('titular', models.ManyToManyField(to='financeiro.usuario')),
            ],
        ),
    ]
