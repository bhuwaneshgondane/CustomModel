from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProjectModelSerializer
from .models import ProjectModel
from  rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='success.log',
# )

logger = logging.getLogger("django")

# Create your views here.
class ProjectCreateAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        obj = ProjectModel.objects.all()
        form = ProjectModelSerializer(obj, many=True)
        logger.info("Reterived the data")
        return Response(data=form.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        form = ProjectModelSerializer(data=request.data)
        if form.is_valid():
            form.save()
            logger.info("Record Added")
            return Response(data=form.data, status=status.HTTP_201_CREATED)
        return Response(data=form.errors,  status=status.HTTP_404_NOT_FOUND)

class ProjectDetailAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request, pk=None):
        try:
            obj= ProjectModel.objects.get(pk=pk)
        except Exception as e:
            return Response(data= {"message": "Details Not Found"})
        serializer = ProjectModelSerializer(instance=obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
             obj= ProjectModel.objects.get(pk=pk)
        except:
             return Response(data= {"message": "Record Not Found"})
        form = ProjectModelSerializer(instance=obj,data=request.data)
        if form.is_valid():
            form.save()
            logger.info("Full Record Updated")
            return Response(data=form.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=form.errors, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,pk):
        try:
             obj= ProjectModel.objects.get(pk=pk)
        except:
             return Response(data= {"message": "ecord Not Found"})
        form = ProjectModelSerializer(instance=obj,data=request.data)
        if form.is_valid():
            form.save()
            logger.info("Partial Record Update")
            return Response(data=form.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(data=form.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        try:
            obj = ProjectModel.objects.get(pk=pk)
        except :
            return Response({"Message":"record not found"})
        obj.delete()
        logger.info("Record Delete")
        return Response(data={"message":"Data Deleted Successfully"},status=status.HTTP_202_ACCEPTED)
