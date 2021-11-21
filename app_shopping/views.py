from django.views.generic import FormView
import pandas as pd

from . import forms

from . import scraping2 as b

import json
import requests


class IndexView(FormView):
    form_class = forms.TextForm
    template_name = "index.html"



    def form_valid(self, form):
        data = form.cleaned_data
        search = data["search"]

        # if request.method == 'POST':
        #         if "" in request.POST:
        # # ①
        #            print("確定ボタンが押下された")
        #         elif "min"  in request.post:
        # # ②
        #             print("キャンセルボタン押下された")
        data_rakuten = b.sea(search)

        kekka = "楽天"


        ctxt = self.get_context_data(data_rakuten=data_rakuten, kekka="検索結果_"+kekka, form=form)
        return self.render_to_response(ctxt)
