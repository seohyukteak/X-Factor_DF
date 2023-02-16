
from django.urls import path
from web.views import base_views
from common import views

urlpatterns = [
    path('', views.login, name=''),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout/'),
    path('updateform/', views.updateform, name='updateform'),
    path('update/', views.update, name='update'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    ########################### x-factor-DF ##########################################
    path('webQuery_DF/', base_views.dataFabric_webQuery, name='webQuery_DF'),
    path('monitoring_DF/', base_views.dataFabric_monitoring, name='monitoring_DF'),
    path('Navigator_DF/', base_views.dataFabric_Navigator, name='Navigator_DF'),
    path('dashboard/query_content/', base_views.dataFabric_api, name='DF_api')
]