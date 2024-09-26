from django.shortcuts import render


def login(request):
    return render(request, 'templates/accounts/login-page.html')


def register(request):
    return render(request, 'templates/accounts/register-page.html')


def profile_delete(request, pk: int):
    return render(request, 'templates/accounts/profile-delete-page.html')


def profile_details(request, pk):
    return render(request, 'templates/accounts/profile-details-page.html')


def profile_edit(request, pk: int):
    return render(request, 'templates/accounts/profile-edit-page.html')
