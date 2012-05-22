from openid.consumer.consumer import Consumer, SUCCESS
from openid.extensions import ax
from django.http import HttpResponse
from django.shortcuts import redirect
from parole2.settings import AUTHORIZED_EMAILS

class BasicOpenidAuthMiddleware:

    def process_request(self, request):
        if request.path_info[0:7] != '/admin/':
            return None

        if 'openid_username' not in request.session:
            request.session['openid_session'] = {}
            consumer = Consumer(request.session['openid_session'], None)

            # auth request to google has not been made yet
            if 'openid.mode' not in request.REQUEST:
                ax_request = ax.FetchRequest()
                ax_request.add(ax.AttrInfo('http://axschema.org/contact/email', required = True))

                auth_request = consumer.begin('https://www.google.com/accounts/o8/id')
                auth_request.addExtension(ax_request)

                url = auth_request.redirectURL(
                    request.build_absolute_uri('/'),
                    return_to=request.build_absolute_uri())
                return redirect(url)
            # auth request has been made, thus analyse google response
            else:
                info = consumer.complete(request.REQUEST, request.build_absolute_uri())
                if info.status == SUCCESS:
                    ax_response = ax.FetchResponse.fromSuccessResponse(info)
                    username = ax_response.get('http://axschema.org/contact/email')[0]
                    request.session['openid_username'] = username

        username = request.session.get('openid_username', None)
        if username not in AUTHORIZED_EMAILS:
            if username: del request.session['openid_username']
            return HttpResponse('403 Forbidden', status=403)
