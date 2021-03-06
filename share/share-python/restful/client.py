#-*- coding: utf-8 -*-
import os
import requests

from share.config import load_yaml


DATA_FORMAT_MAP = {
    'json': 'json'
}


def _get_config():
    base = os.environ['BASE']
    return load_yaml(os.path.join(base, 'avalon.yaml'))


class BaseClient(object):
    def __init__(self, path, subdomain, domain=None, port=None,
                 https=False, data_format='json'):
        self.path_list = path if isinstance(path, (list)) else [path]
        self.subdomain = subdomain
        self.https = https
        self.data_format = data_format

        config = _get_config()
        self.domain = domain or config['DOMAIN']
        self.port = port or config['NGINX']['LISTEN']

    @property
    def _url(self):
        if self.https:
            return 'https://%s.%s%s/%s' % (
                self.subdomain,
                self.domain,
                '' if self.port in (80, '80') else ':' + str(self.port),
                self._path
            )
        else:
            return 'http://%s.%s%s/%s' % (
                self.subdomain,
                self.domain,
                '' if self.port in (80, '80') else ':' + str(self.port),
                self._path
            )

    @property
    def _path(self):
        return '/'.join(self.path_list) + (
            ('.%s' % DATA_FORMAT_MAP[self.data_format])
            if self.path_list else '')

    def __getattr__(self, key):
        return self.__class__(
            self.path_list + [key], self.subdomain, self.domain,
            self.port, self.https
        )

    @property
    def _access_token(self):
        raise NotImplementedError()

    def get(self, **kwargs):
        kwargs['access_token'] = self._access_token
        return requests.get(
            self._url, params=kwargs).json()['result']

    def post(self, **kwargs):
        kwargs['access_token'] = self._access_token
        return requests.post(
            self._url, data=kwargs).json()['result']

    def put(self, **kwargs):
        kwargs['access_token'] = self._access_token
        return requests.put(
            self._url, params=kwargs).json()['result']

    def delete(self, **kwargs):
        kwargs['access_token'] = self._access_token
        return requests.delete(
            self._url, params=kwargs).json()['result']

    def __repr__(self):
        raise NotImplementedError()
        return ('client<%s>: /' % self.subdomain) + self._path
