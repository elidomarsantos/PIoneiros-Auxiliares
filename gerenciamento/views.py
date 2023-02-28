from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Gerais, Comissão
from .forms import Form_Gerais, Form_Comissão
from django.contrib import messages
from django.views import View
from fillpdf import fillpdfs
import os
from django.conf import settings
from django.http import FileResponse, HttpResponseBadRequest

# Create your views here.
def home(request):
    return render(request, 'cp/home.html') 



def publicadores(request):
    
    if request.method == 'POST':
        form1 = Form_Gerais(request.POST)
       
    
        if form1.is_valid() :
            form1.save()       
            messages.info(request, 'Inserido com sucesso')
            form1 = Form_Gerais()
         
        

    else:
        form1 = Form_Gerais()
       
    nome_filtro = request.GET.get('nome')
    anunciado_filtro = request.GET.get('anunciado')      
    
    anciãos = Comissão.objects.all()
    
    if nome_filtro:
        gerais = Gerais.objects.filter(nome__icontains=nome_filtro)
        
    elif anunciado_filtro:
        gerais = Gerais.objects.filter(anunciado__icontains=anunciado_filtro)  
          
    else:
        gerais = Gerais.objects.order_by('nome').all()    
        
    context = {
        'form1': form1, 
        'gerais': gerais,  
        'anciãos': anciãos,
        
    }
        
    return render(request, 'cp/publicadores.html', context) 

def editar_lista(request, id):
    editar = get_object_or_404(Gerais, pk=id)
    form = Form_Gerais(instance=editar)
 
    if request.method == 'POST':
        form = Form_Gerais(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/publicadores')
   
        else:
            return render(request, 'cp/editar_lista.html', {'form':form ,'editar': editar})  


    return render(request, 'cp/editar_lista.html', {'form':form ,'editar': editar}) 

def add_comissão(request):
    
    if request.method == 'POST':
        gerais = Form_Comissão(request.POST)
        
        if gerais.is_valid() :
            gerais.save()
            gerais = Form_Comissão()

            messages.info(request, 'Inserido com sucesso')
            return redirect('/publicadores')
 
    else:
        gerais = Form_Comissão()
    
    return render(request, 'cp/add_comissão.html', {'gerais': gerais})   
 

def editar_comissão(request, id):
    editar = get_object_or_404(Comissão, pk=id)
    form = Form_Comissão(instance=editar)
 
    if request.method == 'POST':
        form = Form_Comissão(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/publicadores')
   
        else:
            return render(request, 'cp/editar_comissão.html', {'form':form ,'editar': editar})  


    return render(request, 'cp/editar_comissão.html', {'form':form ,'editar': editar})  

def deletar_publicador(request, id):
    deletar = get_object_or_404(Gerais, pk=id)
   
    if request.method == 'POST':
        deletar.delete()

        messages.info(request, 'Apagado com sucesso')
        return redirect('/publicadores')

    return render(request, 'cp/deletar_publicador.html')   

def deletar_todos (request):
    del_todos = Gerais.objects.all()
   
    if request.method == 'POST':
        del_todos.delete()

        messages.info(request, 'Apagado com sucesso')
        return redirect('/publicadores')

    return render(request, 'cp/deletar_publicador.html')  
  
def deletar_comissão(request, id):
    deletar = get_object_or_404(Comissão, pk=id)
   
    if request.method == 'POST':
        deletar.delete()

        messages.info(request, 'Apagado com sucesso')
        return redirect('/publicadores')

    return render(request, 'cp/deletar_comissão.html')   


def petição(request, id):
    gerais = get_object_or_404(Gerais, pk=id)
    comissão = get_object_or_404(Comissão) 
    formgerais = Form_Gerais(instance=gerais)
    formcomissão = Form_Comissão(instance=comissão)
    gerais1 = Gerais.objects.all()
   
    
    nome = formgerais['nome'].value()
    nome_mais = nome.upper()
    mês_Inicial = formgerais['mês_Inicial'].value()
        
    mês_Final = formgerais['mês_Final'].value()
    ano_Inicial = formgerais['ano_Inicial'].value()
    ano_Final = formgerais['ano_Final'].value()
    tempo_indeterminado = formgerais['tempo_indeterminado'].value()
    if mês_Inicial is None:
        mês_Inicial = ''
    if mês_Final is None:
        mês_Final = ''    
    if ano_Inicial is None:
       ano_Inicial = ''
    if ano_Final is None:
        ano_Final = ''    
    
    if tempo_indeterminado == 'Sim':
        tempo_indeterminado = "X"
        a = ''
        de = ''
        mês_Inicial = "Contínuo"
        
        
    else:    
        tempo_indeterminado = '' 
        a = 'a'
        de = 'de'
  
            
    data1 = formgerais['data'].value()
    data = data1.strftime("%d-%m-%Y")
    coordenador = formcomissão['coordenador'].value()
    secretário = formcomissão['secretário'].value()
    serviço = formcomissão['serviço'].value()
 
  
    data_dict = {
                
                "nome": nome,
                "mês_Inicial": mês_Inicial,
                'mês_Final': mês_Final,
                'ano_Inicial': ano_Inicial,
                'ano_Final': ano_Final,
                'tempo_indeterminado': tempo_indeterminado,
                'data': data,
                'coordenador': coordenador,
                'secretário': secretário,
                'serviço': serviço,
                'a': a,
                'de': de,
                'nome_mais': nome_mais
                
            }
                
    fillpdfs.write_fillable_pdf('static/petição.pdf', 'static/pronto.pdf', data_dict)
    
    extensão = '.pdf'
    pasta = 'static/'
    nome_antigo = 'static/pronto.pdf'
    novo_nome = pasta + nome + ' ' + '(' + mês_Inicial + ' ' + str(ano_Inicial) + ')' + extensão 
   

    if os.path.exists(novo_nome):
        os.remove(novo_nome)

    os.rename(nome_antigo, novo_nome)
    
    caminho_arquivo = novo_nome
    
    if tempo_indeterminado == 'Sim':
        novo_nome1 = nome + extensão 
    else:
        novo_nome1 = nome + ' ' + '(' + mês_Inicial + ' ' + str(ano_Inicial) + ')' + extensão 
            

    try:
        response = FileResponse(open(caminho_arquivo, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(novo_nome1)
        return response
    except Exception:
        return HttpResponseBadRequest('Erro ao baixar o arquivo')
    
    return redirect('/publicadores')
    
  
    return render(request, 'cp/petição.html', {'formgerais':formgerais ,'formcomissão': formcomissão, 'gerais': gerais, 'gerais1': gerais1,'comissão': comissão })           