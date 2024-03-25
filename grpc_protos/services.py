from django.contrib.auth.models import User
from django_grpc_framework import generics

from grpc_protos.serializers import UserProtoSerializer
from grpc_protos.views.v1.account import account_pb2

class UserService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer

    def List(self, request, context):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        user_list = account_pb2.UserList(userList=serializer.message)
        return user_list
    