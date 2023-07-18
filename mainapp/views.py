from datetime import datetime
import json
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.urls import reverse
from urllib.parse import urlencode


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('mainapp/news/news.json', 'r', encoding='UTF-8') as file:
            news = json.load(file)['news']
            context['news'] = news
        context["range"] = range(2)
        context["datetime_obj"] = datetime.now()
        print(context)
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"



