from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView)
from .models import Drinks


def home(request):
    context = {
        'drinks': Drinks.objects.all()
    }
    return render(request, "home/index.html", context)


class DrinksListView(ListView):
    model = Drinks
    template_name = 'home/index.html'
    context_object_name = 'drinks'
    ordering = ['-date_posted']


class DrinksDetailView(DetailView):
    model = Drinks


class DrinksCreateView(LoginRequiredMixin, CreateView):
    model = Drinks
    fields = ['name', 'ingredients', 'glassware']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DrinksUpdateView(LoginRequiredMixin, UpdateView):
    model = Drinks
    fields = ['name', 'ingredients', 'glassware']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
