
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from un_user_ms import views
from django.contrib import admin

urlpatterns = [
    path('profile/', views.ProfileCreate.as_view()),
    path('profile/<str:pk>/',views.ProfileEdit.as_view()),
    path('profilesGet/',views.ProfileGet.as_view()),
    path('admin/', admin.site.urls),
]

#urlpatterns = format_suffix_patterns(urlpatterns)