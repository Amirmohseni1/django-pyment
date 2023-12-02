import requests

from payment.core import settings
from payment.core.base import BaseProvider
from payment.utils.exceptions import BankGatewayConnectionError
from payment.utils.validators import (
    ValidatedAmount,
    ValidatedDescription,
    ValidatedMerchant,
)


class Zarinpal(BaseProvider):
    def __init__(self, amount, description, user_id):
        self.amount = amount
        self.description = description
        self.__verify_amount = None
        self.__verify_description = None
        self._merchant = settings.ZARINPAL_MERCHANT
        self._provider_endpoint = settings.ZARINPAL_ENDPOINT
        # metadata
        self.phone_number = None
        self.email = None

    def __verify_data(self):
        verified_amount = ValidatedAmount.check(amount=self.amount)
        verified_description = ValidatedDescription.check(description=self.description)
        ValidatedMerchant.check(merchant=self._merchant, provider="ZARINPAL")
        self.__verified_amount = verified_amount
        self.__verified_description = verified_description

    def data(self):
        self.__verify_data()
        data = {
            "merchant_id": self._merchant,
            "amount": self.__verify_amount,
            "description": self.__verify_description,
            "currency": self._currency,
            "callback_url": self._callback_url,
        }
        return self.send_data(data=data)

    def send_data(self, data):
        try:
            response = requests.post(self._provider_endpoint, json=data, timeout=5)
        except requests.Timeout:
            raise BankGatewayConnectionError()
        except requests.ConnectionError:
            raise BankGatewayConnectionError()
        return response

    def _response_check(self):
        pass

    def _save_response(self):
        pass

    def _authority_link_creator(self):
        pass
