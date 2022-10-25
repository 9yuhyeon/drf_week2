from django.urls import path
from articles import views
urlpatterns = [
    path('', views.ArticleList.as_view(), name='ArticleList'),
    path('<int:article_id>/', views.ArticleDetail.as_view(), name='ArticleDetail'),
]


# 공식문서 urls.py에 있는 코드 : 이것은 사용하지 않는건지? / 사용한다면 어떤 경우에 어떻게 사용하는지?
# urlpatterns = format_suffix_patterns(urlpatterns)