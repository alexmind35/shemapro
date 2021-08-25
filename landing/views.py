from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import ListView

from landing.forms import OrderForm
from landing.models import Order, InfoPage
from telebot.sendmessage import sendTelegram


def page_not(request, exception):
    return render(request, '404.html')


class LandingListView(ListView):
    model = InfoPage
    queryset = InfoPage.objects.all()
    template_name = 'landing/content.html'
    context_object_name = 'page_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm()
        return context






def thanks_page(request):
    price = InfoPage.objects.get()
    if request.POST:
        form = OrderForm(request.POST)
        name = request.POST['name_form']
        phone = request.POST['phone_form']
        email = request.POST['email_form']
        org_name = request.POST['organization_name_form']
        org_address = request.POST['organization_address_form']
        count_images = request.POST['count_images_form']
        quantity = int(count_images) * price.price_page

        element = Order(
            order_name=name,
            order_phone=phone,
            order_email=email,
            order_organization_name=org_name,
            order_organization_address=org_address,
            order_count_images=count_images,
            order_quantity=quantity,
        )
        if form.is_valid():
            element.save()
            sendTelegram(tg_name=name, tg_phone=phone)

            html_content = render_to_string('email/email-send.html',
                                            {'title': 'Новый заказ',
                                             'org_name': org_name,
                                             'name_user': name,
                                             'count_images': count_images,
                                             'amount': quantity,
                                             })
            text_content = strip_tags(html_content)
            email_to_template = EmailMultiAlternatives(
                "Новый заказ",
                text_content,
                settings.EMAIL_HOST_USER,
                [email, settings.EMAIL_HOST_USER]
            )
            email_to_template.attach_alternative(html_content, "text/html")
            email_to_template.send()

            return render(request, 'thanks.html', {'name': name}, {'form': form}, )


    else:
        return redirect('index')

    return render(request, 'landing/content.html', {
        'form': form,
    })
