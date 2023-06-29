"""
2020 Black
developer : #ABS
"""
from django.shortcuts import render, redirect

# for daily visits
def daily_visit_view(request):
    return render(request, 'utils/daily_visit/daily_visit.html', name="daily_visit")

# 404 Error view (Page not found)
def page_not_found_error(request, exception):
    return render(request, 'utils/Error/404.html', status=404)
    
    
# 500 Error view (Server Error)
def server_error(request):
    return render(request, 'utils/Error/500.html', status=404)

