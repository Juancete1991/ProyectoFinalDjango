
from django.urls import path, include
from . import views

app_name = 'gastos'

urlpatterns = [
    path('', views.GastoListView.as_view(), name='list'),
    path('nuevo/', views.GastoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.GastoUpdateView.as_view(), name='update'),
    path('<int:pk>/borrar/', views.GastoDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.GastoDetailView.as_view(), name='detail'),
    path('exportar_csv/', views.exportar_csv, name='exportar_csv'),
    path('registro/', views.registro, name='registro'),
]
