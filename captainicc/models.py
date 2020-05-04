from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profession(models.Model):

    libelle_prof = models.CharField(max_length=200,verbose_name="Profession")


    def __str__(self):
        return self.libelle_prof


class Questionnaire(models.Model):

    question = models.CharField(max_length=200,verbose_name="Question")

    def __str__(self):
        return self.question

class Pays(models.Model):

    libelle_pays = models.CharField(max_length=50,verbose_name="Pays")
    
    class Meta:    
        verbose_name_plural = "Pays" 

    def __str__(self):
        return self.libelle_pays


class CategoryMembre(models.Model):

    type_membre = models.CharField(max_length=50,verbose_name="Type de Membre")
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de creation")

    def __str__(self):
        return self.type_membre

class PoleDepartement(models.Model):
    nom_pole = models.CharField(max_length=50,verbose_name="Pole")
    description_pole = models.TextField(verbose_name="Description")
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False,
    verbose_name="Date de creation")
    p_departement = models.ForeignKey('Departement',null=True,blank=True,on_delete=models.CASCADE,verbose_name="Departement")

    def __str__(self):
        return self.nom_pole

class Departement(models.Model):
    nom_dpt = models.CharField(max_length=100,verbose_name="Departement")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.nom_dpt
    

class TypeDon(models.Model):
    libelle_don = models.CharField(max_length=50,verbose_name="Dons")
    models.DateTimeField(auto_now_add=True, auto_now=False,
    verbose_name="Date de creation")

    def __str__(self):
        return self.libelle_don


class Ville(models.Model):
    nom_ville = models.CharField(max_length=30,verbose_name="Ville")
    v_pays = models.ForeignKey('Pays',blank=False,default=1,on_delete=models.CASCADE,verbose_name="Pays")

    def __str__(self):
        return self.nom_ville


class Reponse(models.Model):
    reponse = models.CharField(max_length=100,verbose_name="Reponse")
    r_question = models.ForeignKey('Questionnaire',null=True,blank=True,on_delete=models.CASCADE,verbose_name="Question")

    def __str__(self):
        return 'Question {} : Reponse {} '.format(self.r_question.question,self.reponse)

class Membre(models.Model):

    SEXE_M = 'M'
    SEXE_F = 'F'

    SITUATION_CELI = 'CELIBATAIRE'
    SITUATION_MAR = 'MARIE(E)'
    SITUATION_SEP = 'SEPARE'
    SITUATION_CPT = 'COUPLE'
    SITUATION_DIV = 'DIVORCE'
    SITUATION_PAC = 'PACSE'
    SITUATION_VEU = 'VEUF'
    
    SEXE_CHOICES = (
        (SEXE_M,'Masculin'),
        (SEXE_F, 'Feminin'),
    ) 

    

    SITUATIONS_CHOICES = (
        ( SITUATION_CELI, 'CELIBATAIRE' ),
        ( SITUATION_MAR , "MARIE(E)" ),
        ( SITUATION_SEP , "SEPARE(E)" ),
        ( SITUATION_CPT , "EN COUPLE" ),
        ( SITUATION_DIV , "DIVORCE(E)" ),
        ( SITUATION_PAC , "PACSE(E)" ),
        ( SITUATION_VEU , "VEUF(VE)" ),
    
    )

    mb_nom = models.CharField(max_length=50,verbose_name = "Noms")
    mb_prenoms = models.CharField(max_length=50,verbose_name="Prenoms")
    mb_date_naissance = models.DateField(null=True, blank=True,verbose_name="Date de naissance")

    #mb_telephone = models.CharField( max_length=15,verbose_name="Telephone")
    #mb_mobile = models.CharField(max_length=15,blank=True,verbose_name="Mobile")
    
    mb_mobile = PhoneNumberField(region="FR",verbose_name="Mobile")
    mb_telephone = PhoneNumberField(region="FR",verbose_name="Télephone")

    mb_email = models.EmailField(verbose_name="Email")
    mb_code_postal = models.IntegerField(blank=True,verbose_name="Code postale")
    mb_adresse = models.CharField(max_length=300,verbose_name="Adresse")
    mb_sexe = models.CharField(max_length=20,
                              default=SEXE_M,
                              choices=SEXE_CHOICES,verbose_name="Sexe")
    mb_photo = models.ImageField(default='default-avatar.png',upload_to='profiles_img',verbose_name="Photo de profile")                          
    #mb_photo = models.CharField(max_length=300,default="https://lh6.googleusercontent.com/proxy/GXgmdB-sGQOAA00_z8pVXE8esduRqmr_h349VXgH3S9wUML4joGAbUVkS2F4OGOtTlp2vWTohUM57XyMmyHkAQW13sYUXKpUUq0wIJyz8mk5qkVbPEklXXcJO73UzynDxfbC94Op")
    mb_categoryMembres = models.ForeignKey('CategoryMembre',default=1,blank=False,on_delete=models.CASCADE,verbose_name ="Type de Membre")
    mb_ville = models.ForeignKey('Ville',null=True,blank=True,on_delete=models.CASCADE,verbose_name="Ville")
    mb_profession = models.ForeignKey('Profession',null=True,blank=True,on_delete=models.CASCADE,verbose_name="Profession")


    mb_situation = models.CharField(max_length=100,default=SITUATION_CELI,choices=SITUATIONS_CHOICES,verbose_name="Situation")
    mb_dons = models.ManyToManyField('TypeDon',through='MembresDon')
    mb_pole = models.ManyToManyField('PoleDepartement',through='MembresDepartement')
    mb_reponse = models.ManyToManyField('Questionnaire',through='ReponsesMembre')
    mb_created_at = models.DateField(verbose_name="Date d'ajout",default=timezone.now)

    class Meta:
        verbose_name = "Membre"
        

    def __str__(self):
        return '{} - {}'.format(self.mb_nom,self.mb_prenoms)


class MembresDepartement(models.Model):

    d_membre = models.ForeignKey('Membre',null=True, blank=True,on_delete=models.CASCADE,verbose_name="ID Membre")
    d_pole = models.ForeignKey('PoleDepartement',null=True, blank=True,on_delete=models.CASCADE,verbose_name="ID Pole")
    date_creation = models.DateField(auto_now_add=True,verbose_name="Date de  creation")

    def __str__(self):
        return '{} - {}'.format(self.d_membre.mb_nom,self.d_membre.mb_prenoms)


class ReponsesMembre(models.Model):
    r_reponse = models.TextField(verbose_name="Reponse")
    r_date_creation = models.DateField(auto_now_add=True,verbose_name="Date de creation")
    r_membre = models.ForeignKey('Membre',null=True,blank=True,on_delete=models.CASCADE,verbose_name="ID Membre")
    r_question = models.ForeignKey('Questionnaire',null=True,blank=True,on_delete=models.CASCADE,verbose_name="ID Question")

class MembresDon(models.Model):
    md_date_creation = models.DateField(auto_now_add=True,verbose_name="Date de creation")
    md_montant = models.FloatField(verbose_name="Montant")
    md_membre = models.ForeignKey('Membre',null=True, blank=True,on_delete=models.CASCADE,verbose_name="ID Membre")
    md_typeDon = models.ForeignKey('TypeDon',null=True, blank=True,on_delete=models.CASCADE,verbose_name="Type de dons")

