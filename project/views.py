from django.shortcuts import render

def loginView(request):
    context = {
        "heading":"Login"
    }
    return render(request,'index.html',context)