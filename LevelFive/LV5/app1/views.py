from django.shortcuts import render
from app1.forms import UserForm, UserProfileInfoForm


def index(request):
    return render(request, 'app1/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app1/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def login(request):
    pass

# Create your views here.
