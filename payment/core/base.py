from abc import ABC, abstractmethod
from django.urls import reverse

from payment.core import settings


class BaseProvider(ABC):
    def __init__(self):
        self._callback_url = reverse("payment:Verify")
        self._currency = settings.CURRENCY

    def _currency_check(self):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def _save_provider_response(self):
        pass

    @abstractmethod
    def _verify_transactions(self):
        pass

    @abstractmethod
    def _save_verify_response(self):
        pass
