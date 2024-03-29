# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

from pyramid.httpexceptions import HTTPServerError
from caliopen.base.helpers.connection import connect_storage
from caliopen.api.base.exception import (ValidationError, AuthenticationError,
                                         AuthorizationError, ResourceNotFound)

from caliopen.api.base.renderer import (TextPlainRenderer, JsonRenderer,
                                        PartRenderer)
from caliopen.api.base.deserializer import json_deserializer

log = logging.getLogger(__name__)


def format_error(exc, request, code, name):
    """Format error message in a structure."""
    msg = exc.args[0] if exc.args else ""
    data = {'code': code, 'name': name, 'message': msg}
    request.response.status_int = code
    return {'error': data}


def validation_error(exc, request):
    """Raise HTTP 400."""
    return format_error(exc, request, 400, 'Validation error')


def authentication_error(exc, request):
    """Raise HTTP 401."""
    return format_error(exc, request, 401, 'Authentication error')


def authorization_error(exc, request):
    """Raise HTTP 403."""
    return format_error(exc, request, 403, 'Authorization error')


def resource_not_found_error(exc, request):
    """Raise HTTP 404."""
    return format_error(exc, request, 404, 'Resource not found')


def internal_server_error(exc, request):
    """Raise HTTP 500 correctly."""
    return format_error(exc, request, 404, 'Internal server error')


def includeme(config):
    """Configure REST API."""
    connect_storage()
    config.commit()

    # configure renderers
    config.add_renderer('text_plain', TextPlainRenderer)
    config.add_renderer('json', JsonRenderer)
    config.add_renderer('simplejson', JsonRenderer)
    config.add_renderer('part', PartRenderer)

    # configure specific views for API errors
    config.add_view(validation_error,
                    context=ValidationError,
                    renderer='simplejson')
    config.add_view(authentication_error,
                    context=AuthenticationError,
                    renderer='simplejson')
    config.add_view(authorization_error,
                    context=AuthorizationError,
                    renderer='simplejson')
    config.add_view(resource_not_found_error,
                    context=ResourceNotFound,
                    renderer='simplejson')
    # config.add_view(internal_server_error,
    #                context=HTTPServerError,
    #                render='simplejson')
    config.add_cornice_deserializer('application/json',
                                    json_deserializer)
    config.commit()
    log.info('Base API configured')
