from django.contrib.auth.models import User
from django_grpc_framework import proto_serializers
from grpc_protos.views.v1.account import account_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = ['id', 'username', 'email', 'groups']