from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index-2',views.index2,name="index-2"),
    path('about-us',views.aboutus,name="about-us"),
    path('service',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
    path('about-us-extend',views.aboutusextend,name="about-us-extend"),
    path('blog-single',views.blogsingle,name="blog-single"),
    path('blog/',views.blog,name="blog"),
    path('error-404',views.error404,name="error-404"),
    path('faqs-extend',views.faqsextend,name="faqs-extend"),
    path('faqs',views.faqs,name="faqs"),
    path('gallery-extend',views.galleryextend,name="gallery-extend"),
    path('gallery-photos-all',views.galleryphotosall,name="gallery-photos-all"),
    path('gallery-photos',views.galleryphotos,name="gallery-photos"),
    path('gallery',views.gallery,name="gallery"),
    path('get-a-quote',views.getaquote,name="get-a-quote"),
    path('megamenu',views.megamenu,name="megamenu"),
    path('product-single',views.productsingle,name="product-single"),
    path('products',views.products,name="products"),
    path('project-single',views.projectsingle,name="project-single"),
    path('projects-extend',views.projectsextend,name="projects-extend"),
    path('service-extend',views.serviceextend,name="service-extend"),
    path('projects',views.projects,name="projects"),
    path('service-single-2',views.servicesingle2,name="service-single-2"),
    path('service-single',views.servicesingle,name="service-single"),
    path('teams',views.teams,name="teams"),
    path('team-single',views.teamsingle,name="team-single"),
    path('typography',views.typography,name="typography"),

    

    

]