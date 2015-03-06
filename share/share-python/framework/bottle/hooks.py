# -*- coding: utf-8 -*-
import simplejson

from bottle import request, response, FormsDict as _dict
from bottle import tonat, urlunquote

from share.session import Session
from share.framework.bottle.engines import memory
from share.framework.bottle.engines import db


def _parse_qsl(qs):
    r = []
    for pair in qs.replace(';', '&').split('&'):
        if not pair:
            continue
        nv = pair.split('=', 1)
        if len(nv) != 2:
            nv.append('')
        key = urlunquote(nv[0].replace('+', ' '))
        value = urlunquote(nv[1].replace('+', ' '))
        r.append((key, value.decode('utf8')))
    return r


class FormsDict(_dict):
    def __getattr__(self, name, default=None):
        try:
            return self.dict[name][-1]
        except (UnicodeError, KeyError):
            return default


def mc_session_id(session_id):
    return 'SESSION::%s' % session_id


def fill_session():
    session = Session(request, request.cookies.session_id)
    session.update(simplejson.loads(
        memory.memcached.get(mc_session_id(session.session_id)) or '{}'))

    request.ukey = session.get('ukey', None)


def save_session():
    if request.session is None:
        return

    from bottle import default_app
    app = default_app()

    memory.memcached.set(
        mc_session_id(request.session.session_id),
        simplejson.dumps(request.session or {}))
    response.set_cookie(
        'session_id', request.session.session_id,
        domain=app.config.domain, path='/'
    )


def db_session_rollback():
    db.session.rollback()


def transfer_form():
    post = FormsDict()
    # We default to application/x-www-form-urlencoded for everything that
    # is not multipart and take the fast path (also: 3.1 workaround)
    if not request.content_type.startswith('multipart/'):
        pairs = _parse_qsl(tonat(request._get_body_string(), 'latin1'))
        for key, value in pairs:
            post[key] = value
        return post

    request.environ['bottle.request.post'] = post

    get = request.environ['bottle.get'] = FormsDict()
    pairs = _parse_qsl(request.environ.get('QUERY_STRING', ''))
    for key, value in pairs:
        get[key] = value
    request.environ['bottle.request.query'] = get
