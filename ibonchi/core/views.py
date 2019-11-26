from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView

from .forms import ProfileForm
from .models import Profile


# Create your views here.
@login_required
def dash(request):
    return render(request, 'dash.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


# Create a form for allowing restaurant owners to create a profile for their restaurant
@login_required
def create_profile(request):
    if request.method == 'POST':
        # profile_form = ProfileForm(request.POST, request)
        # create a form instance and populate it with the data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as requred
            form.cleaned_data
            this_form = form.save(commit=False)
            this_form.user_profile = request.user
            this_form.save()

            return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request, 'profile/create_profile.html', {'form': form})


class ProfileUpdate(UpdateView):
    template_name = 'profile/edit_profile.html'
    model = Profile
    form_class = ProfileForm
    success_url = '/'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('form_id')
        return get_object_or_404(Profile, id=id_)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user_profile = self.request.user
        profile.save()
        return super(ProfileUpdate, self).form_valid(form)

# @login_required
# def edit_profile(request, form_id):
#     user_profile = Profile.objects.get(id=form_id)
#     profile_form = ProfileForm(request.POST, instance=user_profile)
#     if request.method == 'POST':
#         if profile_form.is_valid():
#             profile_form.cleaned_data
#             this_form = profile_form.save(commit=False)
#             this_form.user_profile = request.user
#             this_form.save()
#             return HttpResponseRedirect('dash')
#         else:
#             return render(request, 'profile/edit_profile.html', {'user_profile': user_profile})
#
#     else:
#         return render(request, 'profile/edit_profile.html', {'user_profile': user_profile})
