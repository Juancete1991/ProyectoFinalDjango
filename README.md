# Gasto Diario - Gestor de Gastos Personales

Aplicación web desarrollada con Django para el registro y seguimiento de gastos personales. Permite a los usuarios llevar un control detallado de sus finanzas con categorización, filtros avanzados y exportación de datos.

## Descripción del Proyecto

**Gasto Diario** es una aplicación web que permite a los usuarios:
-  Registrar gastos con descripción, monto, fecha, categoría y notas adicionales o detalles.
-  Visualizar todos sus gastos en una lista paginada
-  Filtrar gastos por mes y categoría
-  Ver el total de gastos según los filtros aplicados
-  Editar y eliminar gastos existentes
-  Exportar sus datos a formato CSV
-  Sistema de autenticación (registro, login, logout) para agregar seguridad y privacidad a su gestión de gastos

## Tecnologías Utilizadas

- **Backend:** Django 5.2.7
- **Frontend:** Bootstrap 5 (Tema Bootswatch Quartz)
- **Base de datos:** SQLite3
- **Lenguaje:** Python 3.13
- **Autenticación:** Django Auth System

## Estructura del Proyecto

```
ProyectoFinalDjango/
├── ProyectoFinal/          # Configuración principal del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
├── gastos/                # Aplicación principal
│   ├── models.py          # Modelo Gasto
│   ├── views.py           # Vistas basadas en clases (CBV)
│   ├── forms.py           # Formularios
│   ├── urls.py            # URLs de la app
│   ├── admin.py           # Configuración del admin
│   └── templates/         # Plantillas HTML
│       ├── gastos/
│       │   ├── base.html           # Template base
│       │   ├── gasto_list.html     # Lista de gastos
│       │   ├── gasto_detail.html   # Detalle de gasto
│       │   ├── gasto_form.html     # Crear/Editar gasto
│       │   └── gasto_confirm_delete.html
│       └── registration/
│           ├── login.html          # Inicio de sesión
│           ├── registro.html       # Registro de usuario
│           └── logged_out.html     # Cierre de sesión
├── db.sqlite3             # Base de datos
├── manage.py              # Script de gestión de Django
└── README.md              # Este archivo
```

## Instalación y Ejecución en Local

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos para ejecutar el proyecto

1. **Clonar el repositorio**
```bash
git clone https://github.com/TU_USUARIO/ProyectoFinalDjango.git
cd ProyectoFinalDjango
```

2. **Crear y activar entorno virtual**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones**
```bash
python manage.py migrate
```

5. **Crear superusuario (opcional, para acceder al admin)**
```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Abrir en el navegador**
```
http://127.0.0.1:8000/
```

## Uso de la Aplicación

### Primera vez
1. Accede a `http://127.0.0.1:8000/registro/` para crear una cuenta
2. Inicia sesión con tus credenciales
3. Comienza a registrar tus gastos

### Funcionalidades principales
- **Crear gasto:** Click en "Nuevo gasto" en la barra de navegación
- **Ver detalles:** Click en "Ver" en cualquier gasto de la lista
- **Editar:** Desde el detalle del gasto, click en "Editar"
- **Eliminar:** Desde el detalle del gasto, click en "Eliminar"
- **Filtrar:** Usa los filtros de mes y categoría en la página principal
- **Exportar:** Click en "Descargar CSV" para exportar tus datos

### Categorías disponibles
- Alimentación
- Transporte
- Educación
- Ocio
- Otros

## Características Técnicas

### Vistas Basadas en Clases (CBV)
- `GastoListView` - Lista paginada con filtros
- `GastoDetailView` - Detalle de un gasto
- `GastoCreateView` - Crear nuevo gasto
- `GastoUpdateView` - Editar gasto existente
- `GastoDeleteView` - Eliminar gasto

### Modelo de Datos
```python
class Gasto(models.Model):
    usuario = ForeignKey(User)
    descripcion = CharField(max_length=200)
    monto = DecimalField(max_digits=10, decimal_places=2)
    fecha = DateField()
    categoria = CharField(choices=CATEGORIAS)
    nota = TextField(blank=True)
```

### Seguridad
- Todas las vistas protegidas con `LoginRequiredMixin`
- Cada usuario solo puede ver/editar/eliminar sus propios gastos
- Protección CSRF en todos los formularios
- Validación de permisos en todas las operaciones

## Panel de Administración

Accede al panel de administración en `http://127.0.0.1:8000/admin/` con las credenciales del superusuario.

Funcionalidades del admin:
- Gestión completa de gastos
- Filtros por categoría y fecha
- Búsqueda por descripción y notas
- Gestión de usuarios

## Autor

**Juan Manuel Rojo**
- Proyecto Final - Desarrollo de sistemas Web Tercero
- Profesor: Cesar Gimenez Lascano
- Fecha: Noviembre 2025

## Licencia

Este proyecto fue desarrollado con fines educativos para la materia de Desarrollo de sistemas Web en el instituto IDRA.
