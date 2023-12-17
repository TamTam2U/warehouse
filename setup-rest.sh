# goto rest folder
cd pyramid

# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# install requirements
./env/Scripts/pip install -e .

# run rest server
./env/Scripts/pserve.exe development.ini --reload

