from django.db import models
from django.utils.translation import gettext_lazy as _
from .settings import DEFAULT_CURRENCY
from abc import ABC, abstractmethod


class AbstractPayment(models.Model):
    """
    The main abstract model is designed for basic transaction information, and in this model,
    there is no relationship with the user model. You can use this model as a template to
    create your own personal models.

    However, if you do not have comprehensive documentation regarding abstract models,
    it is advisable not to use this model, as it may lead to complications in your work.
    """

    class Currency(models.TextChoices):
        IRR = "IRR", "IRR (ریال)"
        IRT = "IRT", "IRT (تومان)"

    class Status(models.TextChoices):
        OK = "OK"
        NOK = "NOK"

    # These fields contain the information to be sent to the payment gateway.
    """
    You can control the currency unit for all transactions by using the variable 
    DEFAULT_CURRENCY in the main project settings. The default unit is IRR 
    (Iranian Rial), and this variable accepts only two units: IRR and IRT.
    """
    currency = models.CharField(
        verbose_name=_("Currency"),
        choices=Currency.choices,
        default=DEFAULT_CURRENCY,
        max_length=3,
        null=True,
        blank=True,
    )
    amount = models.PositiveIntegerField(
        verbose_name=_("Amount"), default=0, null=True, blank=True
    )
    description = models.TextField(_("description"))

    # These fields contain the information sent by the payment gateway.
    status = models.CharField(
        verbose_name=_("Status"),
        choices=Status.choices,
        max_length=3,
        null=True,
        blank=True,
    )
    authority = models.CharField(
        verbose_name=_("Authority ID"),
        max_length=128,
        unique=True,
    )

    # These fields carry information sent by the payment gateway for transaction validation.
    code = models.CharField(
        verbose_name=_("Status Code"),
        max_length=50,
        blank=True,
        null=True,
    )
    ref_id = models.CharField(
        verbose_name=_("Ref ID"),
        max_length=50,
        blank=True,
        null=True,
    )
    card_pan = models.CharField(
        verbose_name=_("Card pan"),
        max_length=20,
        blank=True,
        null=True,
    )
    fee_type = models.CharField(
        verbose_name=_("fee type"),
        max_length=50,
        blank=True,
        null=True,
    )
    fee = models.CharField(
        verbose_name=_("fee"),
        max_length=15,
        blank=True,
        null=True,
    )

    class Meta:
        abstract: True


class AbstractService(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _request_to_provider(self):
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
