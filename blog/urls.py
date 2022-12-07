from django.urls import path
from blog import views
from blog.views import AboutView, BlogView, IndividualPostView

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<slug:myslug>/", IndividualPostView.as_view(), name="post"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", views.ContactView, name="contact"),
]