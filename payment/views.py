from django.shortcuts import rende
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm


def view_that_asks_for_money(request):
    
    # what you want the button to do.
    paypal_dict = {
         'business': 'receiver_email@example.com',
         'amount': '6666.66',
         'item_name': 'name of the item',
         'invoice': 'unique-invoice-id',
         'notifiy_url': 'https://www.example.com' + reverse('paypal-ipn')
         'return_url': 'https://www.example.com/your-return-location/',
         'cancel_return': 'https://www.example.com/your-cancel-return',
         'custom': 'Upgrade all users!' # custom commad to corelate to some function later it`s optional
}
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    return render(request, 'payment.html', context)
         
