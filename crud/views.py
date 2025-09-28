from django.shortcuts import render, redirect, get_object_or_404
from .models import cachorro
from django.http import HttpResponse

def test(request):
    if request.method == 'GET':
        banco = cachorro.objects.all()
        return render(request, 'crud.html', {'banco': banco})
    elif request.method == 'POST':
        inputs = {
            'nome' : request.POST.get('nome'),
            'raca' : request.POST.get('raca')
        }
        print(inputs)
        cadastro = cachorro(
            nome = inputs['nome'],
            raca = inputs['raca']
        )
        cadastro.save()
        return redirect('test')
def deletar_cachorro(request, id):
    Cachorro = get_object_or_404(cachorro, id=id)
    Cachorro.delete()
    return redirect('test')


