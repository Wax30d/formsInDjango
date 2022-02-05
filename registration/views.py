from django.shortcuts import render
from . import forms


def regForm(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have received this form again'
    else:
        html = 'welcome for first time'
    return render(request, 'registration/signup.html', {'html': html, 'form': form})
