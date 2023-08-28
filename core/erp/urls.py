from django.urls import path
from .views.visitas.views import*
from .views.salas.views import*
from .views.parqueo.views import*
from .views.trabajadores.views import*
from .views.views import PageNotFoundView
handler404 = PageNotFoundView.as_view()
app_name = 'erp'
urlpatterns = [
    #VISITAS
    path('visita/create/',CreateViewVisita.as_view(),name="visita_create"),
    path('visita/list/',ListViewVisita.as_view(),name="visita_list"),
    path('visita/update/<int:pk>/',UpdateViewVisita.as_view(),name="visita_edit"),
    path('visita/delete/<int:pk>/',DeleteViewVisita.as_view(),name="visita_delete"),
    #EPS
 
    path('epps/list/',ViewEPPS.as_view(),name="epps_list"),
    # path('visita/update/<int:pk>/',UpdateViewVisita.as_view(),name="visita_edit"),
    # path('visita/delete/<int:pk>/',DeleteViewVisita.as_view(),name="visita_delete"),
    #DELIVERY/COURRIER
    path('delivery/create/',CreateViewDelivery.as_view(),name="delivery_create"),
    path('delivery/update/<int:pk>/',UpdateViewDelivery.as_view(),name="delivery_edit"),
    #SALAS
    path('sala/create/',CreateViewSala.as_view(),name="sala_create"),
    path('sala/list/',ListViewSala.as_view(),name="sala_list"),
    path('sala/update/<int:pk>/',UpdateViewSala.as_view(),name="sala_edit"),
    path('sala/delete/<int:pk>/',DeleteViewSala.as_view(),name="sala_delete"),
    #PARQUEO
    path('parqueo/create/',CreateViewParqueo.as_view(),name="parqueo_create"),
    path('parqueo/list/',ListViewParqueo.as_view(),name="parqueo_list"),
    path('parqueo/update/<int:pk>/',UpdateViewParqueo.as_view(),name="parqueo_edit"),
    path('parqueo/delete/<int:pk>/',DeleteViewParqueo.as_view(),name="parqueo_delete"),
    #TRABAJADORES
    path('trab/create/',CreateViewTrabajador.as_view(),name="trabajador_create"),
    path('trab/list/',ListViewTrabajador.as_view(),name="trabajador_list"),
    path('trab/update/<int:pk>/',UpdateViewTrabajador.as_view(),name="trabajador_edit"),
    path('trab/delete/<int:pk>/',DeleteViewTrabajador.as_view(),name="trabajador_delete"),

]