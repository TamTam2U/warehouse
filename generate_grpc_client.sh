# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# generate grpc admin
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/admin --pyi_out=./rest/rest/grpc_client/admin --grpc_python_out=./rest/rest/grpc_client/admin ./grpc/admin.proto

# generate grpc barangkeluar
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/barangkeluar --pyi_out=./rest/rest/grpc_client/barangkeluar --grpc_python_out=./rest/rest/grpc_client/barangkeluar ./grpc/barangkeluar.proto

# generate grpc barangmasuk
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/barangmasuk --pyi_out=./rest/rest/grpc_client/barangmasuk --grpc_python_out=./rest/rest/grpc_client/barangmasuk ./grpc/barangmasuk.proto

# generate grpc item
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/item --pyi_out=./rest/rest/grpc_client/item --grpc_python_out=./rest/rest/grpc_client/item ./grpc/item.proto

# generate grpc kategori
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/kategori --pyi_out=./rest/rest/grpc_client/kategori --grpc_python_out=./rest/rest/grpc_client/kategori ./grpc/kategori.proto

# generate grpc itemrack
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/itemrack --pyi_out=./rest/rest/grpc_client/itemrack --grpc_python_out=./rest/rest/grpc_client/itemrack ./grpc/itemrack.proto

# generate grpc rack
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/rack --pyi_out=./rest/rest/grpc_client/rack --grpc_python_out=./rest/rest/grpc_client/rack ./grpc/rack.proto

# generate grpc role
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/role --pyi_out=./rest/rest/grpc_client/role --grpc_python_out=./rest/rest/grpc_client/role ./grpc/role.proto

# generate grpc user
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/user --pyi_out=./rest/rest/grpc_client/user --grpc_python_out=./rest/rest/grpc_client/user ./grpc/user.proto
