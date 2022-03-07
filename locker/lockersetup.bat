cd %USERPROFILE%\locker
python-3.9.10-amd64.exe /quiet
set PATH=%PATH%;%APPDATA%\..\Local\Programs\Python\Python39\Scripts;%APPDATA%\..\Local\Programs\Python\Python39
cd wheels
pip install pycparser-2.21-py2.py3-none-any.whl -f ./ --no-index
pip install cffi-1.15.0-cp39-cp39-win_amd64.whl -f ./ --no-index
pip install cryptography-36.0.1-cp36-abi3-win_amd64.whl -f ./ --no-index
cd ..
echo Locker is ready to launch!
