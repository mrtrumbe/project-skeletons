# Basic Python Project Skeleton

Beyond the features common to all the Python project skeletons, the notable 
feature of the basic skeleton is its configuration system. This system
works an awful lot like the django configuration system.

Configuration files are simply python modules. Any variables defined at the
top level of the module get exposed as configuration options.

This gives you a lot of flexibility in how the variables get set. You can
load other python modules and use them to set variables in the top level
module. You can take the current top level variables and pass them to other
module functions as a dict using the globals() function. You can do anything
in python that you like.

This configuration system does assume you have full and exclusive control
of the system you are configuring on. Using this system on a client-facing
system could open security holes or execute malicious code.


## Configuration Setup

You have two options:

  - Set an environment variable telling your project which python module to
    load as the configuration file. In this skeleton, that environment 
    variable is called TESTPKG_CONFIG. This can be easily changed in 
    testpkg.main.conf.
  - Import the testpkg.main.conf module and call load_conf manually.

Either way works.


## Configuration Usage

Import testpkg.main.conf and use the CONFIG variable defined within to
access the configuration. CONFIG is a DictDotWrapper object, allowing you
to use either python dict or python object semantics. So CONFIG['A_SETTING']
and CONFIG.A_SETTING are equivalent.

DictDotWrapper is defined in testpkg.main.conf. It can be useful when 
passing around the confiuration information to other configuration modules 
loaded from your main configuration module.
