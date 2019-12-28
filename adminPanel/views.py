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
        limit = data.get('limit')
        email = data.get('email')
        password = data.get('password')

        try:
            dump = {
                'response': response,
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


class SendInvites(View):
    def get(self, request):
        context = {
            'title': 'Главная'
        }
        return render(request, 'adminPanel/panel.html', context)

    def post(self, request):
        data = request.POST

        kwards = data.get('kwards')
        region = data.get('region')
        email = data.get('email')
        password = data.get('password')

        try:
            dump = {
                'kwards': kwards,
                'region': region,
                'email': email,
                'password': password
            }
            savepath = os.path.join(settings.BASE_DIR, 'dump.json')
            with open(savepath, 'w') as dumpfile:
                json.dump(dump, dumpfile, indent=4)

            click.send_invites(region, kwards, email, password)
        except ValueError:
            print('ValueError')
        except Exception as e:
            print('Exception has occured')
            print(e)
        return redirect('index')


class ReplyInvites(View):
    def get(self, request):
        context = {
            'title': 'Главная'
        }
        return render(request, 'adminPanel/panel.html', context)

    def post(self, request):
        data = request.POST

        email = data.get('email')
        password = data.get('password')

        try:
            dump = {
                'email': email,
                'password': password
            }
            savepath = os.path.join(settings.BASE_DIR, 'dump.json')
            with open(savepath, 'w') as dumpfile:
                json.dump(dump, dumpfile, indent=4)

            click.reply_on_invites(email, password)
        except ValueError:
            print('ValueError')
        except Exception as e:
            print('Exception has occured')
            print(e)
        return redirect('index')
