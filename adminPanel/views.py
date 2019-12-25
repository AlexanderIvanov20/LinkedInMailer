import os
import json
from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.


class Index(View):
    def get(self, request):
        context = {
            'title': 'Главная'
        }
        return render(request, 'adminPanel/panel.html', context)

    def post(self, request):
        data = request.POST
        try:
            dump = {
                'response': data.get('response'),
                'kwards': data.get('kwards'),
                'region': data.get('region'),
                'limit': data.get('limit')
            }
            savepath = os.path.join(settings.BASE_DIR, 'dump.json')
            with open(savepath, 'w') as dumpfile:
                json.dump(dump, dumpfile, indent=4)
        except ValueError:
            print('ValueError')
        except Exception as e:
            print('Exception has occured')
            print(e)
        return render(request, 'adminPanel/panel.html')
