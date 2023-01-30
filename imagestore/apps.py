# coding=utf-8
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ImagestoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imagestore'
    verbose_name = _('Imagestore gallery')
