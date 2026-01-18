from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from snippets.models import Snippet
from snippets.serializers import UserSerializer, SnippetSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from snippets.permissions import IsOwnerOrReadonly
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from snippets.tasks import send_welcome_email

# Create your views here.

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )

@api_view(["GET"])
def index(request):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, context={"request":request})
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]

    # providing highlight action
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    # add extra action to greet user
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def greet(self, request, *args, **kwargs):
        
        return Response(f"hi i am {self.request.user} !")

    # override create to include owner
    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner)
        # send welcome email asynchronously
        send_welcome_email.delay(self.request.user.email)
