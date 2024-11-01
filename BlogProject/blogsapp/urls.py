from django.urls import path
from blogsapp import views

urlpatterns = [
    path('list/', views.BlogList.as_view()),
    # path('<int:id>', views.blog_detail),  
]