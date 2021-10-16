from django.shortcuts import render, get_object_or_404
from .basket import Basket
from store.views import Product
from django.http import JsonResponse

def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        # product quantity
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_quantity=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty': basket_qty})
        return response
