from django.shortcuts import render


def is_CheckloginorRegister(func):
    def inner(request):
        if request.user.is_authenticated:
            return render(request,'LMS/home.html')
        else:
            return func(request)
    return inner

