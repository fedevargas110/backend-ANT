from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from LISTA.views import *

router = SimpleRouter()
router.register(r'people', PeopleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apilist/', include(router.urls)),
#    path('auth/', include('rest_auth.urls')),
#    path('registration/', include('rest_auth.registration.urls')),
]
