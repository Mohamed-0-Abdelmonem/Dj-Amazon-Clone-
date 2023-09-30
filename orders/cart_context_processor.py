from .models import Cart, CartDetail


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, status='InProgress')
        if not created:
            cart_detail = CartDetail.objects.filter(cart=cart)
            return {'cart_data': cart, 'cart_datail_data':cart_detail}
        return {'cart_data':cart}

    else:
        return {}    

