from django.shortcuts import render

#from django.contrib.auth.decorators import login_required

#@login_required
def dome_form(request):
    return render(request, "products/index.html")

#@login_required
def about_dr_kali(request):
      return render(request, "products/about_dr_WU.html")





