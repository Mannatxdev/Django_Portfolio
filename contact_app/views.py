from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Email to Admin
            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=contact.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )

            # Confirmation Email to User
            send_mail(
                subject="Thank you for contacting us",
                message="We received your message. We'll get back to you soon.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact.email],
            )

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'success.html')
