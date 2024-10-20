from audioop import reverse

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView , DetailView , UpdateView , DeleteView

from Petstagram.common.forms import CommentForm
from Petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet


class PetAddPage(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'templates/pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


class PetEditPage(UpdateView):
    model = Pet
    template_name = 'templates/pets/pet-edit-page.html'
    form_class = PetEditForm
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy('pet-details', kwargs={'username': self.kwargs['username'], 'pet_slug': self.kwargs['pet_slug'], })


class PetDeletePage(DeleteView):
    model = Pet
    template_name = 'templates/pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'data': self.get_initial()})
        return kwargs


class PetDetailsPage(DetailView):
    model = Pet
    template_name = 'templates/pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = context['pet'].photo_set.all()
        context['comment_form'] = CommentForm()
        return context
