from django.urls import include, path

from core.files.views import FileStandardUploadApi

urlpatterns = [
    path(
        "upload/",
        include(
            (
                [
                    path("standard/", FileStandardUploadApi.as_view(), name="standard"),
                ],
                "upload",
            )
        ),
    )
]