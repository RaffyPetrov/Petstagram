from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from Petstagram.accounts.forms import AppUserCreationForm, ProfileEditForm
from Petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'templates/accounts/login-page.html'


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'templates/accounts/register-page.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'templates/accounts/profile-delete-page.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'templates/accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        photos_with_likes = self.object.photo_set.annotate(likes_count=Count('like'))
        context['total_likes_count'] = sum(photo.likes_count for photo in photos_with_likes)
        context['total_pets_count'] = self.object.pet_set.count()
        context['total_photos_count'] = self.object.photo_set.count()

        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'templates/accounts/profile-edit-page.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
                }
        )
