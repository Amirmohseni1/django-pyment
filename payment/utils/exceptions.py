class PaymentException(Exception):
    """AZ bank gateways exception"""


class MerchantDoesNotCorrect(PaymentException):
    """The requested currency does not support"""


class DescriptionDoesNotCorrect(PaymentException):
    """The requested currency does not support"""


class CurrencyDoesNotSupport(PaymentException):
    """The requested currency does not support"""


class AmountDoesNotSupport(PaymentException):
    """The requested amount does not support"""


class BankGatewayConnectionError(PaymentException):
    """The requested gateway connection error"""


class BankGatewayRejectPayment(PaymentException):
    """The requested bank reject payment"""


class BankGatewayTokenExpired(PaymentException):
    """The requested bank token expire"""


class BankGatewayUnclear(PaymentException):
    """The requested bank unclear"""


class BankGatewayStateInvalid(PaymentException):
    """The requested bank unclear"""


class BankGatewayAutoConnectionFailed(PaymentException):
    """The auto connection cant find bank"""
