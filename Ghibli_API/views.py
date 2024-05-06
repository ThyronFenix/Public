from django.http import JsonResponse
from models import User
import json


def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', '')
        email = data.get('email', '')
        role = data.get('role', '')
        if username and email:
            user = User.objects.create(username=username, email=email)
            return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email, 'role': user.role}, status=201)
        else:
            return JsonResponse({'error': 'Nombre de usuario o correo invalido'}, status=400)


def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'role': user.role} for user in users]
        return JsonResponse(user_list, safe=False)


def get_user(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=user_id)
            user_data = {'id': user.id, 'username': user.username, 'email': user.email, 'role': user.role}
            return JsonResponse(user_data)
        except User.DoesNotExist:
            return JsonResponse({'Error': 'Usuario no encontrato'}, status=404)


def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        username = data.get('username', user.username)
        email = data.get('email', user.email)
        role = data.get('role', user.role)
        user.username = username
        user.email = email
        user.role = role
        user.save()
        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email, 'role': user.role})


def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'Usuario eliminado exitosamente'}, status=204)


def ghibli_api(request):
    if request.method == 'GET':
        role = request.GET.get('role', None)
        if role:
            users = User.objects.filter(role=role)
            user_list = [{'id': user.id,'username': user.username, 'email': user.email, 'role': user.role} for user in users]
            return JsonResponse(user_list, safe=False)
        else:
            return JsonResponse({'error': 'Role incorrecto o no existe'}, status=404)
