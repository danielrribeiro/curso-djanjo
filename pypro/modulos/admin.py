from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modulos.models import Modulo


@admin.register(Modulo)
class Modulo(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')

