from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage
from .models import Category, Good


# def index(request, cat_id):
#     if cat_id is None:
#         cat = Category.objects.first()
#     else:
#         cat = Category.objects.get(pk=cat_id)
#     goods = Good.objects.filter(category=cat).order_by('name')
#     s = "Category: " + cat.name + "<br><br>"
#     for good in goods:
#         s = s + "(" + str(good.pk) + ") " + good.name + "<br>"
#     return HttpResponse(s)

# def index(request, cat_id):
#     cats = Category.objects.all().order_by("name")
#     if cat_id == None:
#         cat = Category.objects.first()
#     else:
#         cat = Category.objects.get(pk=cat_id)
#     goods = Good.objects.filter(category=cat).order_by("name")
#     return render(request, "page/index.html", {"categoty": cat, "cats": cats, "goods": goods})

def index(request, cat_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    if cat_id is None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=cat_id)
    # paginator = Paginator(Good.objects.filter(category=cat).order_by("name"), 10)
    paginator = Paginator(Good.objects.filter(category=cat).order_by("name"), 1)
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
    return render(request, "page/index.html", {"category": cat, "cats": cats, "goods": goods})


# def good(request, good_id):
#     try:
#         good = Good.objects.get(pk=good_id)
#     except Good.DoesNotExist:
#         raise Http404
#     s = good.name + "<br><br>" + good.category.name + "<br><br>" + good.description
#     if not good.in_stock:
#         s = s + "<br><br>" + "Not in the stock!"
#     return HttpResponse(s)

def good(request, good_id):
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    return render(request, "page/good.html", {"cats": cats, "good": good})
