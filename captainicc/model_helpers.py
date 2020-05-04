from captainicc.models import MembresDepartement,Membre

def get_Membre_and_pole():

    membres = Membre.objects.all()
    poles = MembresDepartement.objects.all()


    return membres, poles