import urlparse
from django import template
from django.template.defaulttags import URLNode, url

from parole2.settings import PAROLE2_DOMAIN

register = template.Library()

class AbsoluteURLNode(URLNode):
    def render(self, context):
        path = super(AbsoluteURLNode, self).render(context)
        domain = "http://%s" % PAROLE2_DOMAIN
        return urlparse.urljoin(domain, path)

@register.tag(name='absurl')
def absurl(parser, token, node_cls=AbsoluteURLNode):
    """Just like {% url %} but ads the domain of the current site."""
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar)
