from landing.models import InfoPage


def info_page(request):
    page_context = InfoPage.objects.get()
    return {
        "page_context_price": page_context.price_page,
        "page_context_phone": page_context.phone_page,
    }
