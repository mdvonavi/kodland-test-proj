
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CreatePostView
#from .views import HomePageView

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    #path('', HomePageView.as_view(), name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)