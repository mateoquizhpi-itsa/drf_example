from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
def test(request):
    return Response({'mensaje': 'ok'})


# api de prueba token
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'mensaje': 'prueba de token exitosa!!!'})
