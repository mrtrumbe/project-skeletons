# Python Project Skeleton


## Requirements

Each skeleton flavor will bring in their requirements via pip. However, there are some system dependencies required.

- setuptools
- virtualenv
- pip
- wheels


## Git Ignore

The .gitignore for python projects is in the root py/ directory. Copy it into your project directory once it's created to use it.


## Common Features

All of the python project templates share some common features.


### build.sh/build.bat

The build script at the root of each skeleton flavor is responsible for both setting up your project for development purposes and for building your project into a wheel for deployment. 

If you just want to get developing, call the script without any arguments. This will create a virtualenv for the project, pull in the project requirements, and setup the environment for development.

Call the script with -h or -? to get more information what it can do.


### vrun.sh/vrun.bat

The vrun script at the root of each skeleton flavor is intended to help you run scripts in the bin/ or Script/ folder created by virtualenv. The script's function is very simple:

  1. Source the contents of .env, if it exists, using bash or windows shell.
  2. Call the script given as the first argument to the vrun script.
  3. Pass any additional arguments to the script being called.

This script is mostly a convenience for running commands in a development environment, allowing you to setup the environment for your project using a .env file rather than setting your environment system-wide. You could easily do the same by sourcing .env in your shell before running commands in bin/ or Scripts/.

In production, you'll likely want to find a different way of doing this. For example, on Ubuntu, you might use the /etc/default/ directory to specify the environment for an /etc/init.d/ service that calls your python code.


### setup.py

The setup.py file at the root of each skeleton flavor defines the setuptools package for your project. See setuptools documentation for more information about how to properly fill out the file for your project.

One common reason for editing this file is listing your project's dependencies. Do this with the install_requires parameter. You can also give requirement "extras" using the extras_require parameter. This lets you say, for example, I need the extra requirements for the dev environment.


### requirements.txt

This file tells pip how to actually retrieve the requirements for your project. You should give the same requirements you put in your setup.py file and specify which version of each you want. You can also tell pip where to get the packages to install. See the pip docs for more information on how this works.

