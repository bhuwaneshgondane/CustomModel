from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UserSerializer
from .models import User

# Create your views here.
class AddAPI(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    