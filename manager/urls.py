from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin, name="manager"),
    path('create/',views.createData, name="create"),
    path('logout/',views.logoutView, name="logout"),
    path('delete/<int:delete_id>',views.deleteData, name="delete"),
    path('update/<int:update_id>',views.updateData, name="update"),
]
