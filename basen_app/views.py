from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _


# Create your views here.
def home(request):
    return render(request, 'home.html')


def basen(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        if email and message:
            try:
                send_mail(
                    subject=f'Nowa wiadomość ze strony Basenów od {email}',
                    message=message,
                    from_email='messengerproject64@gmail.com',
                    recipient_list=['7777erik777@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Wiadomość została wysłana pomyślnie!')
            except Exception as e:
                messages.error(request, 'Wystąpił błąd podczas wysyłania wiadomości.')
        else:
            messages.error(request, 'Proszę wypełnić wszystkie pola.')

        return redirect('basen')

    return render(request, 'basen.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        if email and message:
            # Email sending
            try:
                # Translatable subject line
                subject = _('New message from {email}').format(email=email)

                send_mail(
                    subject=subject,
                    message=message,
                    from_email='messengerproject64@gmail.com',
                    recipient_list=['7777erik777@gmail.com'],  # Change to target address
                    fail_silently=False,
                )
                # Translatable success message
                messages.success(request, _('Message has been sent!'))
            except Exception as e:
                # Translatable error message
                messages.error(request, _('An error occurred while sending the message.'))

            return redirect('contact')

    return render(request, 'contact.html')


def aboutUs(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        if email and message:
            try:
                send_mail(
                    subject=f'Nowa wiadomość ze strony O Firmie od {email}',
                    message=message,
                    from_email='messengerproject64@gmail.com',
                    recipient_list=['7777erik777@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Wiadomość została wysłana pomyślnie!')
            except Exception as e:
                messages.error(request, 'Wystąpił błąd podczas wysyłania wiadomości.')
        else:
            messages.error(request, 'Proszę wypełnić wszystkie pola.')

        return redirect('about-us')

    return render(request, 'about_us.html')


def gallery(request):
    """
    View function for the gallery page that also handles email submissions
    from the footer contact form.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        if email and message:
            try:
                # Translatable subject line
                subject = _('New message from Gallery page: {email}').format(email=email)

                send_mail(
                    subject=subject,
                    message=message,
                    from_email='messengerproject64@gmail.com',  # Use your configured email
                    recipient_list=['7777erik777@gmail.com'],  # Target email address
                    fail_silently=False,
                )
                # Success message
                messages.success(request, _('Message has been sent!'))
            except Exception as e:
                # Error message
                messages.error(request, _('An error occurred while sending the message.'))
        else:
            # Missing fields message
            messages.error(request, _('Please fill in all fields.'))

        return redirect('gallery')  # Redirect back to gallery page

    # If it's a GET request, just render the gallery template
    return render(request, 'gallery.html')
