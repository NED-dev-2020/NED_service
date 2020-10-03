from django.contrib import admin

from .models import InstagramImage, Accueil_1Entete, Accueil_2Entete, PhotosProfessionnelle, PhotosPackshot, PhotosNature, PhotosBabyShoot, PhotosMariage, PhotosSeancesShooting, Suggestion, Reservation, NosServiceAccueil, ImagePub, ImagePage1, ImagePage2, ImagePage3

#==========================mes class admin=================================
class InstagramImageAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(InstagramImage, InstagramImageAdmin)

#==========================================================================
class Accueil_2EnteteAdmin(admin.ModelAdmin):
	list_display = ['titre','image','text','date']

admin.site.register(Accueil_2Entete, Accueil_2EnteteAdmin)

class Accueil_1EnteteAdmin(admin.ModelAdmin):
	list_display = ['titre','image','text','date']

admin.site.register(Accueil_1Entete, Accueil_1EnteteAdmin)
#===========================================================================

#===========================================================================
class PhotosProfessionnelleAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(PhotosProfessionnelle, PhotosProfessionnelleAdmin)

class PhotosPackshotAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(PhotosPackshot, PhotosPackshotAdmin)

class PhotosNatureAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(PhotosNature, PhotosNatureAdmin)

class PhotosBabyShootAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(PhotosBabyShoot, PhotosBabyShootAdmin)

class PhotosMariageAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(PhotosMariage, PhotosMariageAdmin)

class PhotosSeancesShootingAdmin(admin.ModelAdmin):
	list_display = ['image','description','date']

admin.site.register(PhotosSeancesShooting, PhotosSeancesShootingAdmin)

#===============suggestion==============
class SuggestionAdmin(admin.ModelAdmin):
      list_display = ['nom' , 'text','date']
      

admin.site.register(Suggestion, SuggestionAdmin)

#=============rerendez-vous ===============
class ReservationAdmin(admin.ModelAdmin):
      list_display = ['nom' ,'tel', 'email' , 'text','date']
      list_filter = ( 'nom', 'tel','date',)

admin.site.register(Reservation, ReservationAdmin)
#============nos services===========
class NosServiceAccueilAdmin(admin.ModelAdmin):
      list_display = ['titre', 'text', 'image']

admin.site.register(NosServiceAccueil, NosServiceAccueilAdmin)
#======================pub===============================
class ImagePubAdmin(admin.ModelAdmin):
      list_display = ['image']

admin.site.register(ImagePub, ImagePubAdmin)
#===========background des trois pages=========
class ImagePage1Admin(admin.ModelAdmin):
      list_display = ['image']

admin.site.register(ImagePage1, ImagePage1Admin)

class ImagePage2Admin(admin.ModelAdmin):
      list_display = ['image']

admin.site.register(ImagePage2, ImagePage2Admin)

class ImagePage3Admin(admin.ModelAdmin):
      list_display = ['image']

admin.site.register(ImagePage3, ImagePage3Admin)
