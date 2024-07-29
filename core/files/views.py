from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.mixins import ApiAuthMixin
from core.files.services import FileStandardUploadService



class FileStandardUploadApi(ApiAuthMixin, APIView):
    def post(self, request):
        service = FileStandardUploadService(user=request.user, file_obj=request.FILES["file"])
        file = service.create()

        return Response(data={"id": file.id}, status=status.HTTP_201_CREATED)