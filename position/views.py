from .models import Position
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PositionSerializer

# Create your views here.

@api_view(['GET'])
def allPositions(request):
    positions = Position.objects.all()
    serializer = PositionSerializer(positions, many=True)
    return Response(serializer.data)