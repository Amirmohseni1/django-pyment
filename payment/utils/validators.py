from abc import ABC, abstractmethod

from payment.core import settings
from payment.utils.exceptions import (
    DescriptionDoesNotCorrect,
    AmountDoesNotSupport,
    MerchantDoesNotCorrect,
)


class Validator(ABC):
    @abstractmethod
    def check(self, amount):
        pass


class ValidatedAmount(Validator):
    @staticmethod
    def check(amount):
        if isinstance(amount, int) and amount > settings.MINIMUM_AMOUNT:
            return amount
        else:
            raise AmountDoesNotSupport()


class ValidatedMerchant(Validator):
    @staticmethod
    def check(merchant, provider):
        if not hasattr(settings, f"{provider}_MERCHANT"):
            raise MerchantDoesNotCorrect()


class ValidatedDescription(Validator):
    @staticmethod
    def check(description):
        if isinstance(description, str) and description:
            return description
        else:
            raise DescriptionDoesNotCorrect()
