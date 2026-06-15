from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # Allowed for all type of users
    # permission_classes = [AllowAny]
    # open for anybody
    # permission_classes = [IsAdminUser]
    # Only for staff users
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authenticated access or read only access
    # permission_classes = [DjangoModelPermissions]
    # permission should be assigned from admin account to specific user
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # similar but unauthorize have read access
