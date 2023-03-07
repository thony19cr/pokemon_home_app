from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse_lazy

from owner.forms import OwnerForm
from owner.models import Owner

from django.db.models import F, Q

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def list_owner(request):

    # data_context = {
    #     'nombre': 'Jesús de La Cruz',
    #     'edad': 29,
    #     'pais_nacimiento': 'Perú',
    #     'dni': '951456123',
    #     'vigente': False
    # }

    data_context = [
        {
            'nombre': 'Jesús de La Cruz',
            'edad': 26,
            'pais_nacimiento': 'Perú',
            'dni': '451456653',
            'vigente': True,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                },
            ]
        },
        {
            'nombre': 'Eduardo Gutierrez',
            'edad': 28,
            'pais_nacimiento': 'Brasil',
            'dni': '46514561',
            'vigente': True,
            'pokemons': []

        },
        {
            'nombre': 'María Luisa',
            'edad': 35,
            'pais_nacimiento': 'México',
            'dni': '23456123',
            'vigente': True,
            'pokemons': []
        }
    ]

    """Crear un objeto en una tabla de la BD"""
    #p = Owner(nombre="Juliana", pais="España", edad=26)
    #p.save()  # Guarda el registro en la B.D.

    #p.nombre = "Samanta"
    #p.save()

    """Obtener todos los elementos de una tabla de la BD"""
    #owners = Owner.objects.all()

    """Filtración de datos: .filter()"""
    #owners = Owner.objects.filter(nombre="Paolo")

    """Filtración de datos con AND de SQL: filter()"""
    #owners = Owner.objects.filter(nombre="Juliana", edad=26)

    """Filtración de datos más precisos con : __contains"""
    #owners = Owner.objects.filter(nombre__contains="Benito")

    """Filtración de datos más precisos con: __endswith"""
    #owners = Owner.objects.filter(nombre__endswith="ima")

    """Obtener un solo objeto de la tabla en la BD"""
    #owners = Owner.objects.get(dni="63451234")

    #print("El dato es: {}".format(owners))
    #print("Tipo de datos: {}".format(type(owners)))

    """Ordenar por cualquier atributo o campo de la tabla"""

    """Ordenar alfabéticamente por nombre"""
    # owners = Owner.objects.order_by('-edad')

    """Ordenar concatenando diferentes métodos de ORMs"""
    #owners = Owner.objects.filter(nombre="Juliana").order_by("-edad")

    """Acortar datos: Obtener un rango de registro de una talba en la BD"""
    owners = Owner.objects.all()[0:5]

    """Eliminando un conjunto de datos es específico"""
    #owners = Owner.objects.filter(id=3)
    #owners.delete()

    """Actualización de datos en la BD a un cierto grupo de datos o un solo registro"""
    #Owner.objects.filter(nombre__startswith="Sam").update(pais="Colombia")


    """Utilizando F expressions"""
    #Owner.objects.filter(edad__lte=27).update(edad=F('edad') + 10)

    """Consultas complejas"""
    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Col')
    #owners = Owner.objects.filter(query)

    """Negar Q"""
    #query = Q(pais__startswith='Pe') & ~Q(edad=23)
    #owners = Owner.objects.filter(query, edad=17)

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Col')
    owners = Owner.objects.filter(query, edad=17)

    """Error de consulta con Q, no es válido"""
    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Col')
    #owners = Owner.objects.filter(edad=17, query)

    return render(request, 'owner/owner_list.html', context={'data': owners})


def owner_search(request):
    query = request.GET.get('q', '')

    print("Query: {}".format(query))
    #owners = Owner.objects.all

    results = (
        Q(nombre__icontains=query)
    )

    if query:
        data_context = Owner.objects.filter(results).distinct()
    else:
        data_context = ''

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})


def owner_details(request):
    """Obtiene todos los elementos de una tabla de la BD"""
    owners = Owner.objects.all()

    return render(request, 'owner/owners_details.html', context={'data': owners})


def owner_create(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']

        form.save()
    else:
        form = OwnerForm()

    return render(request, 'owner/owner-create.html', {'form': form})


def owner_delete(request, id_owner):
    print("ID: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return redirect('owner_list')


def owner_edit(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_detail')

    return render(request, 'owner/owner_update.html', context={'form': form})


"""Vistas basadas en clases"""
"""ListView"""


class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc.html'


class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner-create.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc')
    template_name = 'owner/owner_confirm_delete.html'