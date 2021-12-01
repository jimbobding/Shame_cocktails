from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

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
    paginate_by = 5


class UserDrinksListView(ListView):
    model = Drinks
    template_name = 'home/user_drinks.html'
    context_object_name = 'drinks'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Drinks.objects.filter(author=user).order_by('-date_posted')


class DrinksDetailView(DetailView):
    model = Drinks


class DrinksCreateView(LoginRequiredMixin, CreateView):
    model = Drinks
    fields = ['name', 'ingredients', 'glassware']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DrinksUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Drinks
    fields = ['name', 'ingredients', 'glassware']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        drinks = self.get_object()
        if self.request.user == drinks.author:
            return True
        return False


class DrinksDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Drinks
    success_url = '/'

    def test_func(self):
        drinks = self.get_object()
        if self.request.user == drinks.author:
            return True
        return False

