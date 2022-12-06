from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    #path('<str:package_name>/', views.SnippetList.as_view(),name='snippets_list'),
    #path('snippets/<int:pk>/', views.snippet_detail),
     #path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name='snippets_details'),
     path('db_data_fetch/<str:packagename>',views.GetDatabase.as_view(),name="database_fetch")
]

urlpatterns = format_suffix_patterns(urlpatterns)