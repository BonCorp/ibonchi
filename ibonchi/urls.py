"""ibonchi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ibonchi.core.views.menu.menu_item import \
    MenuItemList, MenuItemCreate, MenuItemDelete, MenuItemUpdate, MenuItemDetail, MenuImageCreate
from ibonchi.core.views.views import ProfileUpdate
from ibonchi.core.views import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('registration', include('django.contrib.auth.urls')),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/<form_id>', ProfileUpdate.as_view(), name='edit_profile'),
    path('menu_items', MenuItemList.as_view(), name='menu_items'),
    path('create_menuitem', MenuItemCreate.as_view(), name='create_menuitem'),
    path('<int:id>/delete', MenuItemDelete.as_view(), name='delete_menuitem'),
    path('<int:id>/edit', MenuItemUpdate.as_view(), name='update_menuitem'),
    path('<slug:pk>/detail', MenuItemDetail.as_view(), name='detail_menuitem'),
    path('<int:id>/images', MenuImageCreate.as_view(), name='image_menuitem')

]
