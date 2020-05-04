from django.contrib import admin
from captainicc.models import Profession,Pays,Ville,\
                              CategoryMembre,Departement,TypeDon,PoleDepartement,\
                               Questionnaire,Reponse,MembresDepartement,ReponsesMembre,\
                               MembresDon,Membre,Reponse     

# Register your models here.

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    pass


@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ('nom_ville','v_pays',)

@admin.register(CategoryMembre)
class CategoryMembreAdmin(admin.ModelAdmin):
    pass

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    pass
@admin.register(TypeDon)
class TypeDonsAdmin(admin.ModelAdmin):
    pass

@admin.register(PoleDepartement)
class PoleDepartementAdmin(admin.ModelAdmin):
    pass

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass

@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    pass

@admin.register(MembresDepartement)
class MembresDepartementAdmin(admin.ModelAdmin):
    pass

@admin.register(ReponsesMembre)
class ReponsesMembreAdmin(admin.ModelAdmin):
    pass

@admin.register(MembresDon)
class MembresDonAdmin(admin.ModelAdmin):
    pass

@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    exclude = ['mb_dons','mb_reponse','mb_created_at']
    list_display = ('mb_nom','mb_prenoms','mb_mobile','mb_email','mb_categoryMembres')
    
    