from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search') # Redireciona para a tua search_view após sucesso
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})