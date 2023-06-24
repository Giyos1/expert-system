from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from account.models import Student, ExportEmployee
from cart.forms import CartAddProductForm
from shop.forms import ProductCreateFrom, ProductEditForm
from .models import Category, Product
from orders.models import OrderItem, Order


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = categories.get(slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = Product.objects.get(id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


@login_required
def my_products(request, category_slug=None):
    category = None
    categories = []
    try:
        user = ExportEmployee.objects.get(user=request.user)
    except:
        return HttpResponse('bu user, Export qila oladigan rolga ega emas')

    for i in user.products_user.all():
        if i.category not in categories:
            categories.append(i.category)
    products = Product.objects.filter(available=True, user=user)
    if category_slug:
        for i in categories:
            if i.slug == category_slug:
                category = i.slug
                products = products.filter(category__slug=category)
    return render(request, 'shop/product/my_list.html',
                  {'category': category, 'categories': categories, 'products': products})


@login_required
def my_product_detail(request, id, slug):
    product = Product.objects.get(id=id, slug=slug, available=True)
    return render(request, 'shop/product/my_detail.html', {'product': product})


@login_required
def my_product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:my_product_detail', id=product.id, slug=product.slug)
        return render(request, 'shop/product/my_edit.html', {'form': form})
    form = ProductEditForm(instance=product)
    return render(request, 'shop/product/my_edit.html', {'form': form})


class MyClassView(LoginRequiredMixin, ListView):
    template_name = 'shop/product/my_list.html'
    model = Product

    def get_queryset(self):
        exp = ExportEmployee.objects.get(user=self.request.user)
        queryset = Product.objects.filter(user=exp)
        self.slug = self.kwargs['category_slug']
        return queryset

    # `    def get_context_data(self, **kwargs):
    #         context = super(MyClassView, self).get_context_data(**kwargs)
    #         context['category_slug'] = context['category_slug'].filter(Country=64)
    #         category = None
    #         categories = Category.objects.all()
    #         products = Product.objects.filter(available=True)
    #         if category_slug:
    #             category = categories.get(slug=category_slug)
    #             products = products.filter(category=category)
    #         return context`

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = None
        context['category'] = self.slug
        categories = []
        try:
            user = ExportEmployee.objects.get(user=self.request.user)
        except:
            return HttpResponse('bu user, Export qila oladigan rolga ega emas')

        for i in user.products_user.all():
            if i.category not in categories:
                categories.append(i.category)
        products = Product.objects.filter(available=True, user=user)
        if self.slug:
            for i in categories:
                if i.slug == self.slug:
                    category = i.slug
                    products = products.filter(category__slug=category)
        context['categories'] = categories
        context['products'] = products
        return context


@login_required
def my_product_delete(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('shop:my_product_list')


@login_required
def my_product_create(request):
    if request.method == "POST":
        print(request.FILES)
        form = ProductCreateFrom(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = ExportEmployee.objects.get(user=request.user)
            product.save()
            return redirect('shop:my_product_detail', id=product.id, slug=product.slug)
        return render(request, 'shop/product/my_create.html', {'form': form})
    form = ProductCreateFrom()
    return render(request, 'shop/product/my_create.html', {'form': form})


@login_required
def my_order_list(request):
    order_item = OrderItem.objects.filter(accepted=False)
    order_products = []
    for i in order_item:
        if i.product.user.user == request.user:
            order_products.append(i)
    return render(request, 'shop/product/my_order_list.html', {'order_products': order_products})


@login_required
def my_order_accept(request, id):
    OrderItem.objects.filter(id=id).update(accepted=True)
    return redirect('shop:my_order_list')


@login_required
def my_order_reject(request, id):
    order = OrderItem.objects.get(id=id)
    order.delete()
    return redirect('shop:my_order_list')
