# deploy_it 
Simple to use deployer for Python applications

## Introduction
I am not going to repeat what is said in the one liner above. Suffice to say,
deploy_it makes it easy for you to deploy a python application even it has
truckload of 3rd party dependencies. deploy_it leverages on the awesome power
of virtualenv to do the same, but in a totally painless manner. It can also
setup a systemd service, if you think you need one.

## Why Should I care?
- Easily deploy your python app
- Takes care of all the dependencies
- Isolated from the Python ecosystem on target machine
- Ability to run app as service

## Getting Started
- Create an "src" directory and copy your source files onto it
- Change the "config.json" according to your needs
- Run "./build.py" to create the deployer archive
- Go to target system, extract the archive and run "./deploy.py"

## Roadmap  
- Fetch source from Git Service

## Authors
* **Aswin Babu Karuvally** - *Initial work*


## License
This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details

