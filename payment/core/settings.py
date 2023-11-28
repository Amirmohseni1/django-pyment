from django.conf import settings
from django.urls import reverse

"""
    You can control the currency unit for all transactions by using the variable 
    'DEFAULT_CURRENCY' in the main project settings. The default unit is IRR 
    (Iranian Rial), and this variable accepts only two units:
    Default -> 'IRR'
    options : 
    - IRR -> IRAN Riyal
    - IRT -> IRAN Toman
"""
if not hasattr(settings, "DEFAULT_CURRENCY"):
    setattr(settings, "DEFAULT_CURRENCY", "IRR")
DEFAULT_CURRENCY = settings.DEFAULT_CURRENCY

"""
    The 'ZARINPAL_MERCHANT' variable, which must be configured in the main project settings,
    is crucial to avoid any issues in the payment process.
    Make sure to obtain the 'MERCHANT' value by contacting your payment service provider.
"""
if not hasattr(settings, "ZARINPAL_MERCHANT"):
    pass

ZARINPAL_CALLBACK_URL = ""
