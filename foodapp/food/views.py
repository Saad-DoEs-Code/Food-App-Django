from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Items
from django.template import loader
from .form import ItemForm

from django.contrib.auth.decorators import login_required

# Class Based Views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



# Create your views here.
def index(request):
    
    try:
        item_list= Items.objects.all()
        
        context = {
            'item_list': item_list,
        }
        if context:
            return render(request=request, template_name="food/index.html", context=context)
        else: 
            raise Exception("Context Not Found")
    except :
        return None


class IndexListView(ListView):
    model = Items
    template_name = "food/index.html"
    context_object_name = "item_list"
    
    
    
def detail(request, item_id):
    
    item = Items.objects.get(pk= item_id)
    context = {
        "item": item,
    }    
    return render(request, "food/detail.html", context)

class ItemDetailView(DetailView):
    model = Items
    template_name = "food/detail.html"

def create_item(request):
    
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, "food/item-form.html", {"form":form})


class CreateItemView(CreateView):
    
    model = Items
    fields = ["item_name","item_price","item_description", "item_image"]
    template_name = "food/item-form.html"
    
    
    def form_valid(self, form):
        # Set the User (which has sent request) for the current Item Form
        form.instance.user_name = self.request.user 
        return super().form_valid(form)
        

def update_item(request, id):
    
    item = Items.objects.get(id= id)
    # "instance" will pass the info of the Item being updated
    form = ItemForm(request.POST or None, instance=item)
    
    context = {
        "form":form,
        "item":item,
        "is_update":True,
    }
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, "food/item-form.html", context=context)

def delete_item(request, id):
    
    item = Items.objects.get(id=id)
    
    if request.method == "POST":
        # If the user confirmed deletion (POST)
        item.delete()
        return redirect("food:index")
    
    # If GET request
    return render(request, "food/item-delete.html", {"item":item})