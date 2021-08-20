
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UsuarioCreationForm

class SignUpView(CreateView):
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
