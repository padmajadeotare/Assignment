from django.urls import path
from . import views

urlpatterns = [

    # path('home1/',views.home1),
    # path('mform/',views.promodelform),
    path('product/',views.ProductView.as_view()),
]
