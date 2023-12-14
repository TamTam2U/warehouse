# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# generate grpc admin
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/admin --pyi_out=./grpc_server/admin --grpc_python_out=./grpc_server/admin ./grpc/admin.proto

# generate grpc barangkeluar
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/barangkeluar --pyi_out=./grpc_server/barangkeluar --grpc_python_out=./grpc_server/barangkeluar ./grpc/barangkeluar.proto

# generate grpc barangmasuk
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/barangmasuk --pyi_out=./grpc_server/barangmasuk --grpc_python_out=./grpc_server/barangmasuk ./grpc/barangmasuk.proto

# generate grpc item
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/item --pyi_out=./grpc_server/item --grpc_python_out=./grpc_server/item ./grpc/item.proto

# generate grpc kategori
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/kategori --pyi_out=./grpc_server/kategori --grpc_python_out=./grpc_server/kategori ./grpc/kategori.proto

# generate grpc itemrack
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/itemrack --pyi_out=./grpc_server/itemrack --grpc_python_out=./grpc_server/itemrack ./grpc/itemrack.proto

# generate grpc rack
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/rack --pyi_out=./grpc_server/rack --grpc_python_out=./grpc_server/rack ./grpc/rack.proto

# generate grpc role
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/role --pyi_out=./grpc_server/role --grpc_python_out=./grpc_server/role ./grpc/role.proto

# generate grpc user
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/user --pyi_out=./grpc_server/user --grpc_python_out=./grpc_server/user ./grpc/user.proto