from django.db import models
from datetime import datetime
#========================mes models====================================
class InstagramImage(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)
#========================================================================
class Accueil_1Entete(models.Model):
	image = models.ImageField()
	titre = models.CharField(null=True, blank=True, max_length=100)
	text = models.TextField(null=True, blank=True, max_length=200)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

class Accueil_2Entete(models.Model):
	image = models.ImageField()
	titre = models.CharField(null=True, blank=True, max_length=100)
	text = models.TextField(null=True, blank=True, max_length=200)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)
#==============================================================================

#==============================================================================
class PhotosProfessionnelle(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)


class PhotosPackshot(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)


class PhotosNature(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)


class PhotosBabyShoot(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)


class PhotosMariage(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)


class PhotosSeancesShooting(models.Model):
	image = models.ImageField()
	description = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

#========================/////Suggestion==========/=================
class Suggestion(models.Model):
    nom = models.CharField("Nom et Prenom",max_length=40)
    text = models.CharField("Texte",max_length=150)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.nom}  {self.text} {self.date}"
#============rendez-vous======/====
class Reservation(models.Model):
    nom = models.CharField("Votre Nom et Prenom",max_length=40)
    tel = models.IntegerField("Téléphone")
    email = models.EmailField("Votre email ",max_length=40, null=True, blank=True)
    text = models.TextField("Redigez votre rendez-vous tout en précisant la date et l'heure")
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.nom} {self.tel}  {self.email} {self.text} {self.date}"

#=============nos services=============
class NosServiceAccueil(models.Model):
    image = models.ImageField(null=True, blank=True)
    titre = models.CharField(null=True, blank=True, max_length=100)
    text = models.TextField(null=True, blank=True, max_length=400)
    def __str__(self):
        return f"{self.image} {self.titre} {self.text}"
#===============imagepub==================================================
class ImagePub(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"{self.image}"



#==============background des trois pages===============
class ImagePage1(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"{self.image}"
#----------------------------------

class ImagePage2(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"{self.image}"
#---------------
class ImagePage3(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"{self.image}"
