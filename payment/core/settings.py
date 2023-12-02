from django.conf import settings

"""
    You can control the currency unit for all transactions by using the variable 
    'DEFAULT_CURRENCY' in the main project settings. The default unit is IRR 
    (Iranian Rial), and this variable accepts only two units:
    Default -> 'IRR'
    options : 
    - IRR -> IRAN Riyal
    - IRT -> IRAN Toman
"""
if not hasattr(settings, "CURRENCY"):
    setattr(settings, "CURRENCY", "IRR")
CURRENCY = settings.CURRENCY
MINIMUM_AMOUNT = 1000

"""
    The 'ZARINPAL_MERCHANT' variable, which must be configured in the main project settings,
    is crucial to avoid any issues in the payment process.
    Make sure to obtain the 'MERCHANT' value by contacting your payment service provider.
"""

ZARINPAL_MERCHANT = ""
ZARINPAL_CALLBACK_URL = ""
ZARINPAL_ENDPOINT = ""
