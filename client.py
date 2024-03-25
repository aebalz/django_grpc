import grpc
from grpc_protos.utils import message_to_dict
from grpc_protos.views.v1.account import account_pb2, account_pb2_grpc


with grpc.insecure_channel('localhost:50051') as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)

    data = stub.Retrieve(account_pb2.UserRetrieveRequest(id=1))
    json = message_to_dict(data)
    print(json)

    data = stub.List(account_pb2.UserListRequest())
    json = message_to_dict(data)
    print(json)
