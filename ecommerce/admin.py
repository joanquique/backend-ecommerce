from django.contrib import admin
from .models import PerfilUsuario, Producto


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "telefono", "created_at")
    search_fields = ("user__username", "user__email", "telefono")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock", "activo", "created_at")
    list_filter = ("activo",)
    search_fields = ("nombre",)