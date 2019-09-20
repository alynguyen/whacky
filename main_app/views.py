from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Widget, Total
from main_app.forms import WidgetForm

# Create your views here.

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'

def home(request):
  widgets = Widget.objects.all()
  form = WidgetForm()
  total, created = Total.objects.get_or_create(id=1)
  return render(request, 'home.html', {
    'total': total,
    'form': form,
    'widgets': widgets,
  })

def create_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    new_widget = form.save()
  return redirect('home')

