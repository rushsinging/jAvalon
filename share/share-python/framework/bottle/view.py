# -*- coding: utf-8 -*-
from bottle import request


HTTP_METHOD_MAP = {
    'get': 'get',
    'push': 'create',
    'put': 'update',
    'delete': 'delete'
}


class MethodView(object):
    decorators = []
    methods = []

    def __init__(self, *args, **kwargs):
        super(MethodView, self).__init__()

    @classmethod
    def as_view(cls, name=''):
        def view_func(*args, **kwargs):
            cls = view_func.view_class(*args, **kwargs)
            return cls.dispatch_request(*args, **kwargs)

        if cls.decorators:
            for decorator in cls.decorators:
                view_func = decorator(view_func)

        view_func.view_class = cls
        view_func.__name__ = name or cls.__name__ + view_func.__name__
        view_func.__doc__ = cls.__doc__
        view_func.__module__ = cls.__module__
        view_func.methods = cls.methods
        return view_func

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        if not meth:
            raise
        return meth(*args, **kwargs)