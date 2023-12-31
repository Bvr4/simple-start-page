# Generated by Django 4.2.5 on 2023-09-19 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('ligne_id', models.AutoField(primary_key=True, serialize=False)),
                ('emplacement', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('url', models.TextField()),
                ('emplacement', models.IntegerField()),
                ('id_ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startpage.ligne')),
            ],
        ),
    ]
