from django.shortcuts import render, redirect
from frontend.models import Release
from frontend.forms import ContactForm

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages


def index(request):
    """Homepage view"""
    page_vars = {'active_page': 'index'}
    return render(request, "frontend/index.html", page_vars)


def buy(request):
    """Buy online page"""
    buy_online = ['itunes', 'google_play', 'amazon']
    page_vars = {'active_page': 'buy'}
    get_releases(buy_online, page_vars)
    return render(request, 'frontend/releases.html', page_vars)


def online(request):
    """Play online page"""
    play_online = ['spotify', 'apple_music', 'sound_cloud', 'shazam']
    page_vars = {'active_page': 'online'}
    get_releases(play_online, page_vars)
    return render(request, 'frontend/releases.html', page_vars)


def get_releases(options, page_vars):
    releases = []
    for release in Release.objects.all().order_by('-date'):
        releases.append({
            'release': release,
            'links': {x: release.__dict__.get(x) for x in options if release.__dict__.get(x)}
        })

    page_vars['releases'] = releases
    return page_vars


def contact(request):
    """Contact form sending e-mails"""
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission for romanstapleton.com",
                body=content,
                from_email=contact_email,
                to=['romanstapleton@gmail.com', 'kristroma@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()

            messages.add_message(request, messages.SUCCESS, 'Your message has been successfully sent')
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

