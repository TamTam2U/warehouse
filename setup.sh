# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# install requirements
./env/Scripts/pip install -e .

# run migrate
./env/Scripts/alembic upgrade head

# deactivate env
deactivate

# setup rest server
python3 -m venv ./rest/env

# activate env in windows
./rest/env/Scripts/activate.bat

# install requirements
./rest/env/Scripts/pip install -e ./rest

# deactivate env
deactivate

# setup grpc server
cd grpc_server

# create env admin
python3 -m venv ./admin/env

# activate env in windows
./admin/env/Scripts/activate.bat

# install requirements
./admin/env/Scripts/pip install -e ./admin

# deactivate env
deactivate

# create env barangkeluar
python3 -m venv ./barangkeluar/env

# activate env in windows
./barangkeluar/env/Scripts/activate.bat

# install requirements
./barangkeluar/env/Scripts/pip install -e ./barangkeluar

# deactivate env
deactivate

# create env kategori
python3 -m venv ./kategori/env

# activate env in windows
./kategori/env/Scripts/activate.bat

# install requirements
./kategori/env/Scripts/pip install -e ./kategori

# deactivate env
deactivate

# create env barangmasuk
python3 -m venv ./barangmasuk/env

# activate env in windows
./barangmasuk/env/Scripts/activate.bat

# install requirements
./barangmasuk/env/Scripts/pip install -e ./barangmasuk

# deactivate env
deactivate

# create env item
python3 -m venv ./item/env

# activate env in windows
./item/env/Scripts/activate.bat

# install requirements
./item/env/Scripts/pip install -e ./item

# deactivate env
deactivate

# create env itemrack
python3 -m venv ./itemrack/env

# activate env in windows
./itemrack/env/Scripts/activate.bat

# install requirements
./itemrack/env/Scripts/pip install -e ./itemrack

# deactivate env
deactivate

# create env rack
python3 -m venv ./rack/env

# activate env in windows
./rack/env/Scripts/activate.bat

# install requirements
./rack/env/Scripts/pip install -e ./rack

# deactivate env
deactivate

# create env role
python3 -m venv ./role/env

# activate env in windows
./role/env/Scripts/activate.bat

# install requirements
./role/env/Scripts/pip install -e ./role

# deactivate env
deactivate

# create env user
python3 -m venv ./user/env

# activate env in windows
./user/env/Scripts/activate.bat

# install requirements
./user/env/Scripts/pip install -e ./user

# deactivate env
deactivate




