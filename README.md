# Client Python Grpc

#### 1. Download the proto file and client.py 

#### 2. Import it to Visual Studio Code

#### 3. Open teminal and execute the command to install necessary dependencies : pip install grpcio grpcio-tools

#### 4. Then execute this command to generate the code :  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. math_operations.proto

#### 5. Make sure that the java server GRPC is listening, to do that follow the steps in " https://github.com/SoufianeOukattou/JavaGrpc "

#### 6. Run the client.py 
