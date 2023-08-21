import random

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.conf import settings

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.services import send_new_pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_key = ''.join([str(random.randint(0, 9))
                                                for _ in range(12)])

        send_mail(
            subject='Поздравляем c регистрацией',
            message=f'Для завершения регистрации пройдите по ссылке\n'
                    f'http://127.0.0.1:8000/users/verify/{self.object.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ConfirmView(TemplateView):
    def get(self, *args, **kwargs):
        key = self.kwargs.get('key')
        user = User.objects.filter(verification_key=key).first()
        if user:
            user.is_active = True
            user.verification_key = key
            user.save()
            login(self.request, user)

        return redirect('users:reg_success')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_new_pass(request.user.email, new_password)
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('users:login'))

