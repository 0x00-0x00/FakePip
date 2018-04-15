# FakePip
## Exploit sudoer with /usr/bin/pip install *

## How to use
Simply download the setup.py file into remote target and execute this in local folder:
```bash
sudo /usr/bin/pip install . --upgrade --force-reinstall
```

## Demonstration
![Screenshot](img/001.JPG?raw=true)


### Download the setup.py file into remote target
![Screenshot](img/002.JPG?raw=true)


### And execute the following command:
![Screenshot](img/003.JPG?raw=true)


### Then we get our shell back!
![Screenshot](img/004.JPG?raw=true)


## Author
This code is developed and maintained (if possible) by Andre Marques (@zc00l)
Any misuse is not the author responsibility.
