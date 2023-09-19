from django.urls import path
from .views.visitas.views import*
from .views.salas.views import*
from .views.parqueo.views import*
from .views.trabajadores.views import*
from .views.ingre_salidas.views import*
from .views.empresas.views import*
from .views.unidad.views import*
from .views.puesto.views import*
from .views.views import PageNotFoundView
handler404 = PageNotFoundView.as_view()
app_name = 'erp'
urlpatterns = [
    #EMPRESAS
    path('empresa/list/',LisViewEmpresa.as_view(),name="empresa_list"),
    path('empresa/add/',CreateViewEmpresa.as_view(),name="empresa_create"),
    #UNIDAD
    path('unidad/list/',ListViewUnidad.as_view(),name='unidad_list'),
    path('unidad/add/',CreateViewUnidad.as_view(),name='unidad_create'),
    path('unidad/edit/<int:pk>/',UpdateViewUnidad.as_view(),name='unidad_update'),
    path('unidad/delete/<int:pk>/',DeleteViewUnidad.as_view(),name='unidad_delete'),
    #PUESTO
    path('puesto/list/',ListViewPuesto.as_view(),name='puesto_list'),
    path('puesto/add/',CreateViewPuesto.as_view(),name='puesto_create'),
    path('puesto/edit/<int:pk>/',UpdateViewPuesto.as_view(),name='puesto_update'),
    path('puesto/delete/<int:pk>/',DeleteViewPuesto.as_view(),name='puesto_delete'),
    #VISITAS
    path('visita/create/',CreateViewVisita.as_view(),name="visita_create"),
    path('visita/list/',ListViewVisita.as_view(),name="visita_list"),
    path('visita/update/<int:pk>/',UpdateViewVisita.as_view(),name="visita_edit"),
    path('visita/delete/<int:pk>/',DeleteViewVisita.as_view(),name="visita_delete"),
    #ASISTEN EN LA VISITA
    path('visita/asis/add/',CreateViewAsist.as_view(),name="asis_create"),
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
    #INGRESO Y SALIDAS DE TRABAJADORES
    path('ingsal/list/',ListViewIngSal.as_view(),name='ingsal_list'),
    path('ingsal/add/',CreateViewIngSal.as_view(),name='ingsal_create'),
    path('ingsal/edit/<int:pk>/',UpdateViewIngSal.as_view(),name='ingsal_update'),

]