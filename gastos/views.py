from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Gasto
from .forms import GastoForm
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
import csv
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class GastoListView(LoginRequiredMixin,ListView):
    model = Gasto
    template_name = 'gastos/gasto_list.html'
    context_object_name = 'gastos'
    paginate_by = 10

    def get_queryset(self):
        # FILTRAR SOLO LOS GASTOS DEL USUARIO ACTUAL
        qs = super().get_queryset().filter(usuario=self.request.user)

        # --- Filtro por mes ---
        mes = self.request.GET.get('mes')
        if mes:
            try:
                year, month = mes.split('-')
                qs = qs.filter(fecha__year=int(year), fecha__month=int(month))
            except ValueError:
                pass

        # --- Filtro por categoría ---
        categoria = self.request.GET.get('categoria')
        if categoria and categoria != '':
            qs = qs.filter(categoria=categoria)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Valores actuales del filtro
        mes = self.request.GET.get('mes', '')
        categoria = self.request.GET.get('categoria', '')

        # Categorías disponibles (desde el modelo)
        context['categorias'] = Gasto.CATEGORIAS
        context['mes'] = mes
        context['categoria'] = categoria

        # Calcular total de los gastos filtrados
        queryset = self.get_queryset()
        total = queryset.aggregate(Sum('monto'))['monto__sum'] or 0
        context['total_gastos'] = total

        return context
    
  


class GastoCreateView(LoginRequiredMixin,CreateView):
    model = Gasto
    form_class = GastoForm
    template_name = 'gastos/gasto_form.html'
    success_url = reverse_lazy('gastos:list')

    def form_valid(self, form):
        # ASIGNAR EL USUARIO ACTUAL AL GASTO ANTES DE GUARDAR
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class GastoUpdateView(LoginRequiredMixin,UpdateView):
    model = Gasto
    form_class = GastoForm
    template_name = 'gastos/gasto_form.html'
    success_url = reverse_lazy('gastos:list')

    def get_queryset(self):
        # SOLO PUEDE EDITAR SUS PROPIOS GASTOS
        return super().get_queryset().filter(usuario=self.request.user)


class GastoDeleteView(LoginRequiredMixin,DeleteView):
    model = Gasto
    template_name = 'gastos/gasto_confirm_delete.html'
    success_url = reverse_lazy('gastos:list')

    def get_queryset(self):
        # SOLO PUEDE BORRAR SUS PROPIOS GASTOS
        return super().get_queryset().filter(usuario=self.request.user)


class GastoDetailView(LoginRequiredMixin,DetailView):
    model = Gasto
    template_name = 'gastos/gasto_detail.html'
    context_object_name = 'gasto'

    def get_queryset(self):
        # SOLO PUEDE VER SUS PROPIOS GASTOS
        return super().get_queryset().filter(usuario=self.request.user)
    

def exportar_csv(request):
    # Solo si el usuario está logueado
    if not request.user.is_authenticated:
        return HttpResponse("No autorizado", status=403)

    # Preparamos la respuesta HTTP como archivo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gastos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Descripción', 'Monto', 'Fecha', 'Categoría', 'Nota'])

    # SOLO EXPORTAR LOS GASTOS DEL USUARIO ACTUAL
    gastos = Gasto.objects.filter(usuario=request.user).order_by('-fecha')
    for g in gastos:
        writer.writerow([g.descripcion, g.monto, g.fecha, g.get_categoria_display(), g.nota or ''])

    return response


def registro(request):
    """Vista para registrar nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Loguear automáticamente al usuario después de registrarse
            login(request, user)
            return redirect('gastos:list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})