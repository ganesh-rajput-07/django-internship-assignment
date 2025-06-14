from django.urls import path
from .views import public_view, protected_view, login_view

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('login/', login_view),
]
