from django.shortcuts import render


def pet_add_page(request):
    return render(request, 'templates/pets/pet-add-page.html')


def pet_edit_page(request, username: str, pet_slug: str):
    return render(request, 'templates/pets/pet-edit-page.html')


def pet_delete_page(request, username: str, pet_slug: str):
    return render(request, 'templates/pets/pet-delete-page.html')


def pet_details_page(request, username: str, pet_slug: str):
    return render(request, 'templates/pets/pet-details-page.html')
