from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Page
from django.contrib.auth.decorators import login_required
from .forms import PageForm
from django.contrib.auth.forms import UserCreationForm


class IndexView(generic.ListView):
    model = Page
    template_name = "wiki/index.html"


class DetailView(generic.DetailView):
    model = Page
    template_name = "wiki/detail.html"


@login_required
def update_view(request, slug):
    context = {}
    page = get_object_or_404(Page, slug = slug)

    if request.method=='POST':
        form = PageForm(request.POST, request.FILES, instance=page)
    else:
        form = PageForm(instance=page)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + slug)
    context["form"] = form
    return render(request, "wiki/page_form.html", context)


@login_required
def create_view(request):
    context = {}
    form = PageForm(request.POST or None, request.FILES)
    if form.is_valid():

        form.save()
        return HttpResponseRedirect("/")
    else:
        form = PageForm()
    context['form'] = form
    return render(request, 'wiki/page_form.html', context)


@login_required
def delete_view(request, slug):
    context = {}
    form = get_object_or_404(Page, slug = slug)
    if request.method == "POST":
        form.delete()
        return HttpResponseRedirect("/")
    return render(request, "wiki/delete_view.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})