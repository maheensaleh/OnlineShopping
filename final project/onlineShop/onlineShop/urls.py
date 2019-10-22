from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from users import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('mobile/', include("mobile.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path ('register/',include('users.urls')),
    path('Help/', include('Help.urls')),
    path('cart/',login_required(views.Cart.my_cart), name="cart" ),
    path('payment/', login_required(views.Stock.update_stock), name="payment"),
    path('delivery/', views.Delivery.deli, name="delivery"),
    path('congrats/', views.Delivery.deli, name="congrats"),
    path('feedback/', views.render_feedback, name="feedback"),
    path('feedback_view/', views.feedback_display, name="feedback_view"),
]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
