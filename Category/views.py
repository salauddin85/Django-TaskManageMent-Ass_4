from django.shortcuts import render,redirect
from  .forms import CategoryForm

# Create your views here.
def add_category(request):
    category_form = CategoryForm()
    if request.method=='POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('categorypage')
        else:
            category_form = CategoryForm()
    return render(request,'category.html',{'form':category_form})

