from pyexpat import model
from django.forms import ModelForm
from wishlist.models import BarangWishlist

class WishlistForm(ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang','harga_barang','deskripsi']