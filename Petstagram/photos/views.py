from django.shortcuts import render


def photo_add_page(request):
    return render(request, 'templates/photos/photo-add-page.html')


def photo_edit_page(request):
    return render(request, 'templates/photos/photo-edit-page.html')


def photo_details_page(request):
    return render(request, 'templates/photos/photo-details-page.html')
