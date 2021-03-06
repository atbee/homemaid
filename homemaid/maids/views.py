# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Maid


class MaidListView(View):
    def get(self, request):
        content = ''
        maids = Maid.objects.all()
        for maid in maids:
            content += f'<li>{ maid.name }</li>'

        return HttpResponse(content)
