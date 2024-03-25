```bash

PATH_OUTPUT="./"
PATH_PROTOS_DIR="./grpc_protos/views/v1/./"

for proto_file in $(find . -type f -wholename './grpc_protos/views/v1/*/*.proto'); do
    python -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ "$proto_file"
done


```