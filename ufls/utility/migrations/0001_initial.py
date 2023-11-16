# Generated by Django 3.1.3 on 2022-05-07 18:56

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Depending on the system, this will either be its IP address or Printer Queue Name', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('queues', multiselectfield.db.fields.MultiSelectField(choices=[('mainqueue', 'Badge Printer - Main Queue'), ('minor15queue', 'Badge Printer - Minor 15+ Queue'), ('minor14queue', 'Badge Printer - Minor 14-15 Queue'), ('daypassqueue', 'Badge Printer - Day Pass Queue'), ('dealersdenqueue', 'Badge Printer - Dealers Den Queue'), ('blackonly', 'Badge Printer - Black Prints Only'), ('r-frontreg1', 'Receipt Printer - Front of Reg Station 1 Queue'), ('r-frontreg2', 'Receipt Printer - Front of Reg Station 2 Queue'), ('r-frontreg3', 'Receipt Printer - Front of Reg Station 3 Queue'), ('r-frontreg4', 'Receipt Printer - Front of Reg Station 4 Queue'), ('r-frontreg5', 'Receipt Printer - Front of Reg Station 5 Queue'), ('r-frontreg', 'Receipt Printer - Front of Reg Station General Queue'), ('r-backreg', 'Receipt Printer - Back of Reg Picker Station Queue'), ('l-it', 'Label Printer - IT Label Printer Queue')], max_length=25)),
                ('type', models.CharField(choices=[('B', 'Badge Printer [SP75+]'), ('R', 'Receipt Printer [Epson TM88-x]'), ('L', 'Label Printer [Brother]')], max_length=1)),
            ],
        ),
    ]