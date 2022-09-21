from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, PostDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/news/', NewsCreate.as_view(), name='news_create'),
   path('create/articles/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/news', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/update/articles/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]