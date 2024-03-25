
from grpc_protos.services import UserService
from grpc_protos.views.v1.account import account_pb2_grpc

urlpatterns = []

def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)