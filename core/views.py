from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from core import models
from django.core.paginator import Paginator
from django.http import Http404
from core import forms


def index(request):
    atores = models.Atores.objects \
    .filter(show=True) \
    .order_by('-id')

    context = {
        'atores': atores    
    }

    return render(
        request,
        'atores/index.html',
        context    
    )

def detalhes(request, ator_id):
    single_contact = models.Atores.objects.filter(pk=ator_id).first()
    
    if single_contact is None:
        raise Http404()

    site_title = f'{single_contact.primeiro_nome} {single_contact.segundo_nome} -'

    context = {
        'atores': single_contact,
        'site_title': site_title    
    }

    return render(
        request,
        'atores/detalhes.html',
        context
    )

def create(request):
    form_action = reverse('create')
    if request.method == 'POST':
        form = forms.AtoresForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            atores = form.save()
            return redirect('update', ator_id=atores.pk)

        return render(
            request,
            'atores/create.html',
            context
        )
    
    context = {
        'form': forms.AtoresForm()
    }

    return render(
        request,
        'atores/create.html',
        context
    )

def update(request, ator_id):
    atores = get_object_or_404(
        models.Atores, pk=ator_id, show=True
    )
    form_action = reverse('update', args=(ator_id,))
    
    if request.method == 'POST':
        form = forms.AtoresForm(request.POST, request.FILES, instance=atores)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            atores = form.save()
            return redirect('update', ator_id=atores.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': forms.AtoresForm(instance=atores),
        'form_action': form_action,
    }

    return render(
        request,
        'atores/create.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('index')

    atores = models.Atores.objects \
    .filter(show=True) \
    .filter(
        Q(primeiro_nome__icontains=search_value) |
        Q(segundo_nome__icontains=search_value) |
        Q(idade__icontains=search_value) 
    )\
    .order_by('-id') 
    
    paginator = Paginator(atores, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'atores': page_obj,
        'site_title': 'Search -',
        'search_value': search_value,    
    }

    return render(
        request,
        'atores/index.html',
        context
    )

def delete(request, ator_id):
    atores = get_object_or_404(
        models.Atores, pk=ator_id, show=True
    )

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        atores.delete()
        return redirect('index')

    return render(
        request,
        'atores/detalhes.html',
        {
            'atores': atores,
            'confirmation': confirmation   
        }    
    )

