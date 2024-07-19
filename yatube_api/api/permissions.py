from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Проверка на предоставление разрешения
    на просмотр всем пользователям,
    на редактирование или удаление только автору.
    """

    def has_object_permission(self, request, view, obj):

        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
