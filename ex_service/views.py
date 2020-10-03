from django.shortcuts import render

from .models import InstagramImage, Accueil_1Entete, Accueil_2Entete, PhotosProfessionnelle, PhotosPackshot, PhotosNature, PhotosBabyShoot, PhotosMariage, PhotosSeancesShooting, Suggestion, ImagePub, NosServiceAccueil,ImagePage1, ImagePage2, ImagePage3


from .formulaire import SuggestionForm, ReservationForm
#==========================page accueil==============================
def index(request):
    exinst = InstagramImage.objects.all()
    entete1 = Accueil_1Entete.objects.all()
    entete2 = Accueil_2Entete.objects.all()

    album1 = PhotosProfessionnelle.objects.all()
    album2 = PhotosPackshot.objects.all()
    album3 = PhotosNature.objects.all()
    album4 = PhotosBabyShoot .objects.all()
    album5 = PhotosMariage .objects.all()
    album6 = PhotosSeancesShooting.objects.all()

    return render(request, "Pages/index.html", {'insta':exinst, 'tete1':entete1, 'tete2':entete2, 'alb1':album1, 'alb2':album2, 'alb3':album3, 'alb4':album4, 'alb5':album5, 'alb6':album6, 'pub':ImagePub.objects.all(), 'service':NosServiceAccueil.objects.all(),'message':Suggestion.objects.all()})

#===========================page contact==============================
def contact(request):
    exinst = InstagramImage.objects.all()
    if request.method == "POST":
        form = ReservationForm(request.POST).save()
    form = ReservationForm()

    return render(request, "Pages/contact.html", {'form' : form , 'insta':exinst, 'back':ImagePage1.objects.all()})

#===========================page galerie==============================
def galerie(request):
	exinst = InstagramImage.objects.all()


	album1 = PhotosProfessionnelle.objects.all()
	album2 = PhotosPackshot.objects.all()
	album3 = PhotosNature.objects.all()
	album4 = PhotosBabyShoot .objects.all()
	album5 = PhotosMariage .objects.all()
	album6 = PhotosSeancesShooting.objects.all()
	return render(request, "Pages/galerie.html", {'insta':exinst, 'alb1':album1, 'alb2':album2, 'alb3':album3, 'alb4':album4, 'alb5':album5, 'alb6':album6, 'back':ImagePage2.objects.all()})

#===========================page a_propos==============================
def a_propos(request):
    if request.method == "POST":
        form = SuggestionForm(request.POST).save()
    form = SuggestionForm()
    exinst = InstagramImage.objects.all()
    return render(request, "Pages/a_propos.html", {'insta':exinst, 'Sug':form, 'back':ImagePage3.objects.all(),'img1':ImagePage2.objects.all(),'img2':ImagePage3.objects.all()})

