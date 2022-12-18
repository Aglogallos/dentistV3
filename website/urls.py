from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('faq-page=2', views.faq_page2, name='faq-page=2'),
    
    path('blog-details', views.blog_details, name='blog_details'), #replace with jobs
    path('jobs', views.jobs, name='jobs'),

    path('appointment', views.appointment, name='appointment'),
]
