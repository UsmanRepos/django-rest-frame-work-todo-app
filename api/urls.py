from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import TodoViewSet, Login

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls)),
    path('login', Login.as_view())
]