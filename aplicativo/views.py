from django.shortcuts import render, redirect, get_object_or_404
from teste.forms import UsuarioForm, TarefaForm
from teste.models import usuarios, tarefas  # Corrigindo maiúsculas para classes padrão Django

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # Corrigido o redirecionamento
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})  # Verifique se o caminho está correto

def lista_tarefas(request):
    tarefas_list = tarefas.objects.all()  # Corrige o nome para Tarefas
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas_list})

def atualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(usuarios, pk=usuario_id)  # Utilize get_object_or_404 para tratar erros
    if request.method == 'POST':
        usuario.u_nome = request.POST['u_nome']
        usuario.u_email = request.POST['u_email']
        usuario.save()
        return redirect('lista_usuarios')
    else:
        context = {'usuario': usuario}
        return render(request, 'usuarios/atualizar.html', context)

def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(usuarios, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    else:
        context = {'usuario': usuario}
        return render(request, 'usuarios/confirmar_delecao.html', context)

def cadastrar_tarefa(request):
    if request.method == 'POST':
        tarefa = tarefas.objects.create(
            t_codigo=request.POST['t_codigo'],
            t_setor=request.POST['t_setor'],
            usuario=usuarios.objects.get(u_codigo=request.POST['usuario'])
        )
        return redirect('lista_tarefas')
    else:
        form = TarefaForm()
        return render(request, 'tarefas/cadastrar.html', {'form': form})

def lista_usuarios(request):
    try:
        usuario = usuarios.objects.all()
    except Exception as e:
        return render(request, 'usuarios.html', {'erro': e})
    return render(request, 'usuarios.html', {'lista_usuarios': usuario})