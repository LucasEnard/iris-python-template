## iris-python-template
This is a template of InterSystems IRIS Interoperability full Python.

## What The Sample Does

This sample starts an empty production but as all the backbone of the production needed to start coding in Python.

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.


## Installation: Docker
Clone/git pull the repo into any local directory

```
$ git clone https://github.com/intersystems-community/iris-interoperability-template.git
```

Open the terminal in this directory and run:

```
$ docker-compose build
```

Run the IRIS container with your project:

```
$ docker-compose up -d
```

## How to Run the Sample

Open the [production](http://localhost:52795/csp/irisapp/EnsPortal.ProductionConfig.zen?PRODUCTION=dc.Demo.Production) and connect using `SuperUser` and `SYS` then start it.


## How to alter the template 
Use the green "Use this template" button on Github to copy files into a new repository and build a new IRIS interoperability solution using this one as an example.

This repository is ready to code in VSCode with the ObjectScript plugin.
Install [VSCode](https://code.visualstudio.com/), [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) and [ObjectScript](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript) plugin and open the folder in VSCode.

Use the handy VSCode menu to access the production and business rule editor and run a terminal:
<img width="656" alt="Screenshot 2020-10-29 at 20 15 56" src="https://user-images.githubusercontent.com/2781759/97608650-aa673480-1a23-11eb-999e-61e889304e59.png">

## What to alter in the template
If you want to start **coding in Python** access the `src/python` folder.<br>
Here you will find all the code that is used in the production, with examples for almost all kind of object you can create in the Framework ( Business Services, Processes, Operations, Adapters, Messages and more ).

For examples of what is achievable using the Python part, see :
- [The source code of the module and docs on the project](https://github.com/grongierisc/interoperability-embedded-python)
- [A way to use Hugging Face models in IRIS](https://github.com/LucasEnard/iris-local-ml)
- [An implementation of the fix protocol in IRIS](https://github.com/LucasEnard/iris-fix-protocol)
- [A formation that covers database usage, API and CRUD requests in IRIS](https://github.com/LucasEnard/formation-template-python)

