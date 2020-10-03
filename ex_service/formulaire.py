from django.forms import ModelForm
from . models import Reservation
from . models import Suggestion

class ReservationForm(ModelForm):
      class Meta:
           model = Reservation
           fields = [ 'nom', 'tel', 'email', 'text' ]


class SuggestionForm(ModelForm):
      class Meta:
           model = Suggestion
           fields = [ 'nom', 'text' ]
