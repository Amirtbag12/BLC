"""
2020 Black
developer : #ABS
"""
from django.shortcuts import render, redirect


# for All visits
def visit_view(request):
    return render(request, 'utils/visit/visit.html')

# for mounth visits
def mounth_visit_view(request):
    return render(request, 'utils/visit/mounth_visit.html')

# for week visits
def week_visit_view(request):
    return render(request, 'utils/visit/week_visit.html')

# for daily visits
def daily_visit_view(request):
    return render(request, 'utils/visit/daily_visit.html')

# 404 Error view (Page not found)
def page_not_found_error(request, exception):
    return render(request, 'utils/Error/404.html', status=404)
    
    
# 500 Error view (Server Error)
def server_error(request):
    return render(request, 'utils/Error/500.html', status=404)

