from parole2.settings import DEBUG

"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

def paroles_context(request):
    dic = {'parole_domain': 'test' }
    if DEBUG:
        dic['disqus_developer'] = True
