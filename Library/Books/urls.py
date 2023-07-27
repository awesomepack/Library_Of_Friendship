from django.urls import path
from . import views

urlpatterns = [
    #/Books/
    path("" , views.index, name = "index"),
    
    #/Books/9780393347777/
    path("<int:ISBN>/" , views.Book , name="Book"),

    #/Books/9780393347777/Book_Comment/
    path("<int: ISBN>/Book_Comment/" , views.Book_Comment , name = Book_Comment),

    #/Authors/
    path("Authors/", views.Authors , name= "Authors"),

    #/Authors/2/
    path("Authors/<int: id>/" , views.Author , name= "Author"),

    
    
]