import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST


@ensure_csrf_cookie
@require_GET
def csrf(request):
    return JsonResponse({'detail': 'CSRF cookie set.'})


@require_POST
def login_view(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'detail': 'Invalid request.'}, status=400)

    user = authenticate(request, username=data.get('username'), password=data.get('password'))
    if user is None:
        return JsonResponse({'detail': 'Invalid username or password.'}, status=400)

    login(request, user)
    return JsonResponse({'username': user.username})


@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'detail': 'Logged out.'})


@require_GET
def me(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'Not authenticated.'}, status=401)
    return JsonResponse({'username': request.user.username})
