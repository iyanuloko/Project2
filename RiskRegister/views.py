from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RiskRegisterForm
from .models import RiskRegister
from django.http import HttpResponse

@login_required(login_url='login')
def riskRegister(request):
    context = {}
    form1 = RiskRegisterForm()
    if request.POST:
        form1 = RiskRegisterForm(request.POST)
        if form1.is_valid():
            instance = form1.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponse('<h1>Form Saved</h1>')
    context['form1'] = form1
    return render(request, 'personal/RiskReg.html', context)

@login_required(login_url='login')
def submission(request):
    print('Hello, form is submitted.')
    date = request.POST['date']
    category = request.POST['category']
    explanation = request.POST['explanation']
    roles = request.POST['roles']
    riskregister = RiskRegister(date=date, category=category, roles=roles, explanation=explanation)
    riskregister.save()
    return render(request, 'personal/RiskReg.html')
# Create your views here.
