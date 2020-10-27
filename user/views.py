from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import *

from . models import *
from . forms import *


# Create your views here.
class UserListView(ListView):
    queryset = User.objects.all()

class UserCreateView(CreateView):
    template_name = 'user/user_form.html'
    form_class = UserModelForm
    queryset = User.objects.all()

class UserDetailView(DetailView):
    queryset = User.objects.all()

class UserDeleteView(DeleteView):
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse("user:user-list")
