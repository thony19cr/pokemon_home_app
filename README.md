### APP Pokemon

App Pokemon - Gestor de Owners

### Requerimientos
* Python 3.6+
* Django < 4
* Pipenv


#### Configuracion
```
Nota: Se trabajará con el nombre del proyecto para ejecutar los comandos
```

### Crear un entorno virtual e instalar los requerimientos del proyecto
```
pip install -r requeriments.txt
```

### Crear las tablas en nuestra BD para las apps
```
python manage.py makemigrations
python manage.py migrate
```

### Para iniciar el proyecto
```
python manage.py runserver
```

### Test de código y buenas prácticas
```
pip install flake8
```

### Uso de flake8
```
flake8 .
```