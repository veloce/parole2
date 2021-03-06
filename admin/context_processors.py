from parole2.settings import PAROLES_PUB_HOUR

"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

def openid_username(request):
    return {'openid_username': request.session.get('openid_username') }

def pub_hour(request):
    return {'paroles_pub_hour': PAROLES_PUB_HOUR}
