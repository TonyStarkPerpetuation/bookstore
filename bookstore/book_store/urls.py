from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.first_view),
    url(r'^add_book',views.add_book),
    url(r'^book_list',views.book_list),
    url(r'^update_book/(\d+)',views.update_book),
    url(r'^delete_book/(\d+)',views.delete_book),

]


