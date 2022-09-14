from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import BarangWishlist

def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Kak Cinoy'
    }
    return render(request, "wishlist.html", context)

def get_all_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize('xml',data), content_type='application/xml')

def get_all_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize('json',data), content_type='application/json')

def get_one_xml(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml',data), content_type='application/xml')

def get_one_json(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json',data), content_type='application/json')

