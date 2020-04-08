from django.shortcuts import render,redirect

def alowed_user(allowed=[]):
    def decorator(view_func):
        def warp(request, *args, **kwargs):
            if request.user.usertype in allowed:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')
        return warp
    return decorator