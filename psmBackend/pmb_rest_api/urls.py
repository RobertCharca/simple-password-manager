
#All about rest_framework
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UsersViewSet, 'users')

urlpatterns = router.urls