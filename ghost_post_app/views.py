from django.shortcuts import render, HttpResponsePermanentRedirect, reverse
from ghost_post_app.models import BoastRoast
from ghost_post_app.forms import PostForm
from rest_framework import viewsets
from ghost_post_app.serializer import BoastRoastSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all().order_by('-timeposted')
    serializer_class = BoastRoastSerializer

    @action(detail=False)
    def boasts(self, request):
        queryset = BoastRoast.objects.filter(choices = True)
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        queryset = BoastRoast.objects.filter(choices = True)
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvotes += 1
        post.save()
        return Response({'status': post.upvotes})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvotes += 1
        post.save()
        return Response({"status": post.downvotes})

    @action(detail=False)
    def totalvotes(self, request):
        sort_by_votes = sorted(BoastRoast.objects.all(), key=lambda x: x.totalvotes, reverse=True)
        serializer = self.get_serializer(sort_by_votes, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['post'])

