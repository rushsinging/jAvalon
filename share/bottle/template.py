# -*- coding: utf-8 -*-
import os
import functools

from bottle import view, Jinja2Template
from bottle import request
from bottle import default_app


def get_template_path():
    app = default_app()
    print app.config.home_path
    base_templates = os.path.join(
        app.config.home_path, 'share/bottle/templates')
    app_templates = os.path.join(app.app_path, 'templates')
    return [base_templates, app_templates]


class Jinja2Template(Jinja2Template):
    def __init__(self, *args, **kwargs):
        lookup = kwargs.setdefault('lookup', [])
        if callable(lookup):
            kwargs['lookup'] = lookup()
        else:
            kwargs['lookup'] = []
        super(Jinja2Template, self).__init__(*args, **kwargs)


view = functools.partial(
    view,
    template_adapter=Jinja2Template,
    request=request,
    template_lookup=get_template_path
)