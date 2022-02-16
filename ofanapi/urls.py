from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'homes', views.HomesViewSet)
router.register(r'groups', views.GroupsViewSet)
router.register(r'Join_Group', views.Join_GroupViewSet)


urlpatterns = router.urls