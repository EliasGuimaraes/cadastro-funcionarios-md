from django.shortcuts import render
from registermd.models import Publication


# Create your views here.
def render_index(request):
    return render(request, 'index.html', {})


def render_publication_done(request):
    publication_data = {
        'regiao': request.POST.get('regiao'),
        'pais': request.POST.get('pais'),
        'nome': request.POST.get('nome'),
        'cargo': request.POST.get('cargo'),
        'time': request.POST.get('time'),
        'email': request.POST.get('email'),
        'telefone': request.POST.get('telefone'),
        'cpf': request.POST.get('cpf'),
        'data_de_nascimento': request.POST.get('data_de_nascimento')
    }

    publication = Publication(**publication_data)
    publication.save()
    return render(request, 'publication_done.html', {'nome': publication.nome})
