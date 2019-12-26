import os
import json

from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect

import Parser.Click as click


class Index(View):
    def get(self, request):
        context = {
            'title': 'Главная'
        }
        return render(request, 'adminPanel/panel.html', context)

    def post(self, request):
        data = request.POST

        response = data.get('response')
        # kwards = data.get('kwards')
        # region = data.get('region')
        limit = data.get('limit')
        email = data.get('email')
        password = data.get('password')

        try:
            dump = {
                'response': response,
                # 'kwards': kwards,
                # 'region': region,
                'limit': limit,
                'email': email,
                'password': password
            }
            savepath = os.path.join(settings.BASE_DIR, 'dump.json')
            with open(savepath, 'w') as dumpfile:
                json.dump(dump, dumpfile, indent=4)

            click.send_message(limit, email, password, response)
        except ValueError:
            print('ValueError')
        except Exception as e:
            print('Exception has occured')
            print(e)
        return render(request, 'adminPanel/panel.html')
