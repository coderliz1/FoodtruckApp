"""
URL configuration for foodtruck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodtruck import views  # Import views from the foodtruck app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin view
    path('', views.home, name='home'),  # Home page view
    path('trucks/', views.truck_list, name='truck_list'),  # Truck list view
    path('events/', views.event_list, name='event_list'),  # Event list view
    path('search/', views.search_trucks, name='search_trucks'),  # Search trucks view
    path('trucks/<int:truck_id>/calendar/', views.truck_calendar, name='truck_calendar'),  # Truck calendar view
    path('add-event/', views.add_event, name='add_event'),  # New URL for adding an event
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
