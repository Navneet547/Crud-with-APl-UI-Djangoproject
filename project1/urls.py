"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from app1.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', knowledge_base_view_templates.as_view(),name="knowledge"),
#     path('add/',addview.as_view(),name="add"),
#     path('update/<int:id>',update.as_view(),name="update"),
#     path('api/',knowledge_base_view.as_view(),name='api'),
#     path('api/delete/<int:id>',knowledge_base_view.as_view(),name="delete"),
# ]


from django.urls import path
from app1.views import knowledge_base_view, knowledge_base_view_templates, addview, update, deleteView

urlpatterns = [
    path('api/', knowledge_base_view.as_view(), name='api'),
    # path('api/<int:id>/delete/', knowledge_base_view.as_view(), name='apidelete'),

    path('', knowledge_base_view_templates.as_view(), name='knowledge_templates'),
    path('add/', addview.as_view(), name='basicb'),
    path('update/<int:id>/', update.as_view(), name='update'),
    path('delete/<int:id>/',deleteView.as_view(),name="delete")
]
