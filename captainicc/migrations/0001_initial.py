# Generated by Django 3.0.5 on 2020-05-01 18:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMembre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_membre', models.CharField(max_length=50, verbose_name='Type de Membre')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_dpt', models.CharField(max_length=100, verbose_name='Departement')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mb_nom', models.CharField(max_length=50, verbose_name='Noms')),
                ('mb_prenoms', models.CharField(max_length=50, verbose_name='Prenoms')),
                ('mb_date_naissance', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('mb_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='FR', verbose_name='Mobile')),
                ('mb_telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='FR', verbose_name='Télephone')),
                ('mb_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('mb_code_postal', models.IntegerField(blank=True, verbose_name='Code postale')),
                ('mb_adresse', models.CharField(max_length=300, verbose_name='Adresse')),
                ('mb_sexe', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=20, verbose_name='Sexe')),
                ('mb_photo', models.ImageField(default='profilepic.png', upload_to='profiles_img', verbose_name='Photo de profile')),
                ('mb_situation', models.CharField(choices=[('CELIBATAIRE', 'CELIBATAIRE'), ('MARIE(E)', 'MARIE(E)'), ('SEPARE', 'SEPARE(E)'), ('COUPLE', 'EN COUPLE'), ('DIVORCE', 'DIVORCE(E)'), ('PACSE', 'PACSE(E)'), ('VEUF', 'VEUF(VE)')], default='CELIBATAIRE', max_length=100, verbose_name='Situation')),
                ('mb_categoryMembres', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.CategoryMembre', verbose_name='Type de Membre')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_pays', models.CharField(max_length=50, verbose_name='Pays')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_prof', models.CharField(max_length=200, verbose_name='Profession')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='TypeDon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_don', models.CharField(max_length=50, verbose_name='Dons')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ville', models.CharField(max_length=30, verbose_name='Ville')),
                ('v_pays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Pays', verbose_name='Pays')),
            ],
        ),
        migrations.CreateModel(
            name='ReponsesMembre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_reponse', models.TextField(verbose_name='Reponse')),
                ('r_date_creation', models.DateField(auto_now_add=True, verbose_name='Date de creation')),
                ('r_membre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Membre', verbose_name='ID Membre')),
                ('r_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Questionnaire', verbose_name='ID Question')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.CharField(max_length=100, verbose_name='Reponse')),
                ('r_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Questionnaire', verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='PoleDepartement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pole', models.CharField(max_length=50, verbose_name='Pole')),
                ('description_pole', models.TextField(verbose_name='Description')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('p_departement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Departement', verbose_name='Departement')),
            ],
        ),
        migrations.CreateModel(
            name='MembresDon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md_date_creation', models.DateField(auto_now_add=True, verbose_name='Date de creation')),
                ('md_montant', models.FloatField(verbose_name='Montant')),
                ('md_membre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Membre', verbose_name='ID Membre')),
                ('md_typeDon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.TypeDon', verbose_name='Type de dons')),
            ],
        ),
        migrations.CreateModel(
            name='MembresDepartement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField(verbose_name='Date de  creation')),
                ('d_membre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Membre', verbose_name='ID Membre')),
                ('d_pole', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.PoleDepartement', verbose_name='ID Pole')),
            ],
        ),
        migrations.AddField(
            model_name='membre',
            name='mb_dons',
            field=models.ManyToManyField(through='captainicc.MembresDon', to='captainicc.TypeDon'),
        ),
        migrations.AddField(
            model_name='membre',
            name='mb_pole',
            field=models.ManyToManyField(through='captainicc.MembresDepartement', to='captainicc.PoleDepartement'),
        ),
        migrations.AddField(
            model_name='membre',
            name='mb_profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Profession', verbose_name='Profession'),
        ),
        migrations.AddField(
            model_name='membre',
            name='mb_reponse',
            field=models.ManyToManyField(through='captainicc.ReponsesMembre', to='captainicc.Questionnaire'),
        ),
        migrations.AddField(
            model_name='membre',
            name='mb_ville',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='captainicc.Ville', verbose_name='Ville'),
        ),
    ]
