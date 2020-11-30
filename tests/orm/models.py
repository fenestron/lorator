# -*- coding: utf-8 -*-

from lorator.orm import Model


class User(Model):

    __fillable__ = ["name"]
