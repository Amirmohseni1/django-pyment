from django.db import models
from .core.abstracts import AbstractPayment
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Payment(AbstractPayment):
    """
    This model serves as a simple payment model in your database,
    inheriting from the AbstractPayment model. It has the ability
    to establish a relationship with the main user model in your system.
    """

    user = models.ForeignKey(
        verbose_name=_("User"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.user:
            return f"{self.user} - {self.amount}"
        else:
            return f"{self.amount}"

    class Meta:
        app_label = "payment"
        verbose_name = _("payment")
        verbose_name_plural = _("payments")
