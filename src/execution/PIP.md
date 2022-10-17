<h1>PIP</h1>
<h3>Python package manager</h3>
<p>Similar to NPM, allows to install external Python packages and modules.
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
It uninstall Python packages or libraries for Python2 or Python3 whether is set as the default version.  

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
