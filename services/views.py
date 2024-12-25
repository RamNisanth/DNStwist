from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from services.utils.DNS_Service import get_whois_with_dnstwist, save_data_to_excel #user defined function 

@login_required
def myservice(request):
    return render(request, 'services/MyService.html')

@login_required
def option1(request):
    domain = request.GET.get('domain', '')
    return render(request, 'services/option1.html', {'domain': domain})

def option2(request):
    domain = request.GET.get('domain', '')
    return render(request, 'services/option2.html', {'domain': domain})

def option3(request):
    domain = request.GET.get('domain', '')
    return render(request, 'services/option3.html', {'domain': domain})

import os
from django.http import HttpResponse, Http404
from django.conf import settings

def download_page(request):
    # Get the domain parameter from the request
    domain = request.GET.get('domain', 'google.com')
    
    
    generated_file_path = os.path.join(settings.MEDIA_ROOT, 'domain_data.xlsx')
    print("media root", settings.MEDIA_ROOT)

    data = get_whois_with_dnstwist(domain) 

    save_data_to_excel(data, generated_file_path) 

    if not os.path.exists(generated_file_path):
        raise Http404(f"No file found: {generated_file_path}")
    
    return render(request, 'services/download_page.html', {'MEDIA_URL': settings.MEDIA_ROOT})