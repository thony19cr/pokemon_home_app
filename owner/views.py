from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from owner.forms import OwnerForm
from owner.models import Owner

from django.db.models import F, Q


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