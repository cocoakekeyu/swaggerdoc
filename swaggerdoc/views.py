# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings


class DocIndexView(View):

    def get(self, request):

        BASE_DIR = settings.BASE_DIR
        DOC_DIR = getattr(settings, 'DOC_DIR', None)
        if not DOC_DIR:
            DOC_DIR = os.path.join(BASE_DIR, 'docs')

        filenames = [(filename, filename.split('.')[0]) for filename in os.listdir(DOC_DIR)]
        return render(
            request=request,
            template_name='swagger-index.html',
            context={'filenames': filenames},
        )
