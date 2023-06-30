from django.urls import re_path
import .usage as usage


urlpatterns = [
    re_path(r'uptime/$', usage.uptime, name='uptime'),
    re_path(r'memory/$', usage.memusage, name='memusage'),
    re_path(r'cpuusage/$', usage.cpuusage, name='cpuusage'),
    re_path(r'getdisk/$', usage.getdisk, name='getdisk'),
    re_path(r'getusers/$', usage.getusers, name='getusers'),
    re_path(r'getips/$', usage.getips, name='getips'),
    re_path(r'gettraffic/$', usage.gettraffic, name='gettraffic'),
    re_path(r'proc/$', usage.getproc, name='getproc'),
    re_path(r'getdiskio/$', usage.getdiskio, name='getdiskio'),
    re_path(r'loadaverage/$', usage.loadaverage, name='loadaverage'),
    re_path(r'platform/([\w\-\.]+)/$', usage.platform, name='platform'),
    re_path(r'getcpus/([\w\-\.]+)/$', usage.getcpus, name='getcpus'),
    re_path(r'getnetstat/$', usage.getnetstat, name='getnetstat'),
]