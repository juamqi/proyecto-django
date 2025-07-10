from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) 
            return redirect('lista_posts')  
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})