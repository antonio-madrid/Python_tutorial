# Python command line

## Python
It checks what Python interpreter version is in use or if it is installed.
```shell
python --version
```

It checks what Python 3 interpreter version is in use or if it is installed.
```shell
python3 --version
```

It executes Python files with Python 2 or Python 3 if set as a default interpreter.
```shell
python ../main.py
```

## Python3
It executes Python files with Python 3 interpreter.
```shell
python3 ../main.py
```

# PIP
### Python package manager
Similar to NPM, allows to install external Python packages and modules.
Can find PIP packages on https://pypi.org/  

#### PIP usual commands:

It install Python packages or libraries for Python2 or Python3 whether is set as the default version.
```shell
pip install somePackage
```

It installs Python3 packages or libraries  
```shell
pip3 install somePackage
```

<br> 
It uninstall Python packages or libraries for Python2 or Python3 whether it is set as the default version.  

```shell
pip uninstall somePackage
```

It uninstalls Python3 packages or libraries
```shell
pip3 uninstall somePackage
```

<br>
List all Python 2 or Python 3 installed packages

```shell
pip list
```

List all Python 3 installed packages
```shell
pip3 list
```


It shows Python modules already installed.  
<br>

Once a module has been installed, it must be imported for using.
<br>
```shell
pip3 install camelcase
```

```python
# Importing camelcase library
c = camelcase.Camelcase()
```
