from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receita.models import Receita


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('nome não pode ser nulo')
            return redirect('cadastro')
        if not email.strip():
            print('email não pode ser nulo')
            return redirect('cadastro')
        if password != password2:
            messages.error(request, 'As senhas não correspondem')
            print('senhas não correspondem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('Usuário cadastrado com sucesso')
        messages.success(request, 'Cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        if email == "" or password == "":
            print("os campos não podem ser nulos")
            return redirect('login')
        print(email, password)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username = nome, password=password)
            if user is not None:
                auth.login(request, user)
                print('okoko')
        return redirect ('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect ('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')






