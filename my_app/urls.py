from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from my_app.views import EmployeeViewSet, PositionListCreate, PositionRetrieveUpdateDestroy

router = DefaultRouter()
router.register('employees', EmployeeViewSet, 'employees')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/positions/', PositionListCreate.as_view()),
    path('api/positions/<int:pk>/', PositionRetrieveUpdateDestroy.as_view()),
]


