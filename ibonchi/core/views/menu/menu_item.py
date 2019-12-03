from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, DetailView

from ibonchi.core.forms import MenuItemForm, MenuImageForm
from ibonchi.core.models import MenuItem, MenuImage


class MenuItemList(ListView):
    template_name = 'menu/menuitem_list.html'
    model = MenuItem

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'menu/menuitem_create.html'
    form_class = MenuItemForm
    success_url = 'menu_items'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(MenuItemCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class MenuItemDelete(DeleteView):
    template_name = 'menu/menuitem_delete.html'
    model = MenuItem
    success_url = reverse_lazy('menu_items')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MenuItem, id=id_)


@method_decorator(login_required, name='dispatch')
class MenuItemUpdate(UpdateView):
    template_name = 'menu/menuitem_update.html'
    model = MenuItem
    success_url = reverse_lazy('menu_items')
    form_class = MenuItemForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(MenuItem, id=id_)


@method_decorator(login_required, name='dispatch')
class MenuItemDetail(DetailView):
    template_name = 'menu/menuitem_detail.html'
    queryset = MenuItem.objects.all()


@method_decorator(login_required, name='dispatch')
class MenuImageCreate(CreateView):
    model = MenuImage
    template_name = 'menu/menuitem_detail.html'
    form_class = MenuImageForm
    success_url = '/menu_items'

    def form_valid(self, form):
        form.instance.menu_item_id = self.kwargs.get('id')
        form.save(commit=True)
        return super(MenuImageCreate, self).form_valid(form)
