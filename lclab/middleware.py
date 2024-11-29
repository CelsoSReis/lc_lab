from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs permitidas sem autenticação
        allowed_urls = [reverse('login'), reverse('cadastro')]

        if not request.user.is_authenticated:
            if request.path not in allowed_urls:
                return redirect('login')

        response = self.get_response(request)
        return response