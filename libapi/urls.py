from django.urls import path, include
from libapi.views import BookViewset, AuthorCreateView, LoginView, ContactUsView, AuthorListView, AuthorCreateListView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('books', BookViewset)

'''path('books/', BookList.as_view()),
path('books/<int:pk>', BookRetrieve.as_view())'''

urlpatterns = [
    path('', include(router.urls)),
    path('authors', AuthorCreateListView.as_view()),
    path('login', LoginView.as_view()),
    path('contact-us', ContactUsView.as_view())
    # path('authors', AuthorListView.as_view())
]
