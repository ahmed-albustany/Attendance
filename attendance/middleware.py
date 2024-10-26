from django.http import HttpResponseForbidden

class OpenVPNAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        vpn_username = request.META.get('HTTP_X_VPN_USERNAME')
        if vpn_username:
            request.vpn_username = vpn_username
        else:
            return HttpResponseForbidden("Access Denied")

        response = self.get_response(request)
        return response