from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect


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
            # Wysyłanie emaila
            try:
                send_mail(
                    subject=f'Nowa wiadomość od {email}',
                    message=message,
                    from_email='messengerproject64@gmail.com',
                    recipient_list=['7777erik777@gmail.com'],  # Zmień na adres docelowy
                    fail_silently=False,
                )
                messages.success(request, 'Wiadomość została wysłana!')
            except Exception as e:
                messages.error(request, 'Wystąpił błąd podczas wysyłania wiadomości.')

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
