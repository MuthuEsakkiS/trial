from apps.common.views import AppAPIView, NonAuthenticatedAPIMixin


from apps.access.tasks import create_user_dynamically


class CreateUserAPIView(NonAuthenticatedAPIMixin, AppAPIView):
    """API view to create user dynamically by celery task."""

    def get(self, request):
        """GET method to call the `create_user_dynamically` function."""

        create_user_dynamically.delay()
        return self.send_response("Success.")
