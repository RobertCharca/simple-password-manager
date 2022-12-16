
#All about rest_framework
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('user', views.UsersViewSet, 'user')
router.register('category', views.CategoryViewSet, 'category')
router.register('webpage', views.ItemWebPageViewSet, 'webpage')
router.register('card', views.ItemPaymentCardViewSet, 'card')

urlpatterns = router.urls