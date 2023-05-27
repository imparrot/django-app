from django.views import View

import tasks.refer_task.refer_api as refer_api


class ReferView(View):

    def get(self, request, func):
        if func == "home":
            return refer_api.index(request)
        else:
            return refer_api.index(request)

    def post(self, request, func):
        if func == "home":
            return refer_api.index(request)
        else:
            return refer_api.index(request)
