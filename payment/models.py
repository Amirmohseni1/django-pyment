from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    class Meta:
        app_label = _("payment")
        verbose_name = _("payment")
        verbose_name_plural = _("payments")
