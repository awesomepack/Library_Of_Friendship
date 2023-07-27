from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("You will see the books list here")


def Book(request , ISBN):
    return HttpResponse("You are looking at a book's details chosen from the list of books")

def Authors(request ):
    return HttpResponse("You are looking at a list of Authors in the Library")

def Author(request , Author_id):
    return HttpResponse("You are looking at the details of an Author chosen from the Author's list")

def Book_Comment(request , ISBN):
    return HttpResponse("You are writing a comment on a book, maybe your interpretation of it?")
