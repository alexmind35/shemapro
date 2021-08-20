from django.contrib import admin

from landing.models import Order, StatusOrder, InfoPage


class OrderAdm(admin.ModelAdmin):
    list_display = (
        'id', 'order_status', 'order_name', 'order_phone', 'order_email', 'order_organization_name',
        'order_count_images',
        'order_quantity', 'order_date_time')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_date_time')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_date_time', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_date_time')


admin.site.register(Order, OrderAdm)
admin.site.register(StatusOrder)
admin.site.register(InfoPage)
