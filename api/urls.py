from django.urls import path
from api.views import ownArea,regisProduct,setPrice,activateProduct,deactivateProduct,buyProduct
from . import views

"""
urlpatterns = [
    path('ownArea/', views.ownArea, name='ownArea'),
    path('regisProduct/', views.regisProduct, name='regisProduct'),
    path('setPrice/', views.setPrice, name='setPrice'),
    path('activateProduct/', views.activateProduct, name='activateProduct'),
    path('deactivateProduct/', views.deactivateProduct, name='deactivateProduct'),
    path('buyProduct/', views.buyProduct, name='buyProduct')
]

"""
urlpatterns = [
    path('ownArea/', ownArea.as_view()),
    path('regisProduct/', regisProduct.as_view()),
    path('setPrice/', setPrice.as_view()),
    path('activateProduct/', activateProduct.as_view()),
    path('deactivateProduct/', deactivateProduct.as_view()),
    path('buyProduct/', buyProduct.as_view()),
]