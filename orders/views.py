from django.http import HttpResponse
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    """Create an order."""
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Create an order object but don't save it yet
            order = form.save()
            print(cart)
            for item in cart:
                # Create an order item object but don't save it yet
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # Clear the cart
            cart.clear()
            print("cart.clear()")
            return render(request, 'orders/order/created.html', {'order': order})
            # return HttpResponse("order created")
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
    else:
        form = OrderCreateForm()
    return render(request, "orders/order/create.html", {'cart': cart, 'form': form})
