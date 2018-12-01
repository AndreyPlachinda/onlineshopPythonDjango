from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context_processors import csrf
from cart.cart import Cart
from .models import Category, Product
from cart.forms import CartAddProductForm


# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter( available=True )
    if category_slug:
        category = get_object_or_404( Category, slug=category_slug )
        products = products.filter( category=category )
    return render( request, 'product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    } )


# Страница товара
# def ProductDetail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


# def ProductDetail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context = {'product': product, 'cart_product_form': cart_product_form}
#     context.update(csrf(request))
#     return render_to_response('product/detail.html', context)


def ProductDetail(request, id, slug):
    product = get_object_or_404( Product, id=id, slug=slug, available=True )
    cart_product_form = CartAddProductForm()
    CartDetail(request)
    return render( request, 'product/detail.html',
                   {'product': product,
                    'cart_product_form': cart_product_form} )



def CartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    return render(request, 'cart/details.html', {'cart': cart})