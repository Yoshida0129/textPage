from django.shortcuts import render
from .forms import TextForm


def textPage(request):
    form = TextForm
    data = {"text": form}
    return render(request, "./mysite/index.html", data)




