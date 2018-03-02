from django.shortcuts import render


def gallery_list(request):
    return render(request, 'handmade/gallery_list.html', {})
