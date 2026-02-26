from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductCreateView, ProductShowView, ContactPageView, CartView, CartRemoveAllView
from .views import SignupView, LoginView, LogoutView, ImageViewFactory, ImageLocalStorage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("products/", ProductIndexView.as_view(), name="index"),
    path("products/create/", ProductCreateView.as_view(), name="form"),
    path("products/<str:id>", ProductShowView.as_view(), name="show"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        'image/',
        ImageViewFactory(ImageLocalStorage()).as_view(),
        name='image_index'
    ),

    path(
        'image/save',
        ImageViewFactory(ImageLocalStorage()).as_view(),
        name='image_save'
    ),
]