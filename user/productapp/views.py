from django.shortcuts import render,redirect
from . models import *
from . forms import *
from django.views import View


class ProductView(View):
    form_class = ProductForm
    template_name = 'productapp/product.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/')

        return render(request, self.template_name, {'form' : form})
