from django.utils.deprecation import MiddlewareMixin
from .models import Visit
from user_agents import parse
import geoip2.database

class UniqueVisitsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        session_key = request.session.session_key

        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        visit, created = Visit.objects.get_or_create(session_key=session_key)
        visit.increment_visit_count()
        visit.last_visit_url = request.path

        # Capture IP address
        visit.ip_address = self.get_ip_address(request)

        # Capture user agent details
        user_agent = parse(request.META.get('HTTP_USER_AGENT', ''))
        visit.browser = user_agent.browser.family
        visit.browser_version = user_agent.browser.version_string
        visit.os = user_agent.os.family
        visit.os_version = user_agent.os.version_string
        visit.device = user_agent.device.family

        # Save the visit instance
        visit.save()

        request.visit = visit

    def get_ip_address(self, request):
        return request.META.get('HTTP_X_REAL_IP', '')