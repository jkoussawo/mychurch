from django.shortcuts import render,redirect
from captainicc.models import Membre, MembresDepartement
from captainicc.forms import MembreForm
# Create your views here.

def membre_list(request):
    #membres = Membre.objects.all()
    membres = Membre.objects.order_by('mb_nom')
   
    membrePole = MembresDepartement.objects.all() 

    context = {
        'membres' : membres,
        'membrePole' : membrePole ,
    }
    return render(request,'captainicc/membre_list.html',context)

def add_membre(request):
    

    if request.method == 'POST':
        membreForm = MembreForm(request.POST,request.FILES)

        if membreForm.is_valid():
             membreForm.save()
             print(membreForm.instance)

             return redirect('membres-list')
    else:
        membreForm = MembreForm()

    # Envoyer des modeles.
    context = {
        'membreForm' : membreForm ,
        
    }

    return render(request,'captainicc/add_membre.html',context )

def list_membre_profile(request):
    membres = Membre.objects.all()

    context = {
        'membres' : membres,
    }
    return render(request,'captainicc/profile.html',context)