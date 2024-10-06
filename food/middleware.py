from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

from accounts.models import BlackListedIPAddresses


class GetIPAddressesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))


class BlockIPAddress(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        check_ip = BlackListedIPAddresses.objects.filter(ip_address=ip).exists()
        if check_ip:
            return HttpResponse('You are blocked from this site')