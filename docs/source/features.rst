Features
========

I want to setup hdl-utils for a project that already exists.
------------------------------------------------------------

.. code-block:: gherkin

   Given:  User has existing directory structure.
    When:  User adds __init__.py file in each directory containing VHDL files
     And:  User adds __init__.py file in each parent directory
     And:  User executes hdl-utils
    Then:  hdl-utils searches for directories with __init__.py files
    Then:  hdl-utils updates __init__.py files with HDL file information

I want to set properties on files
---------------------------------

.. code-block:: gherkin

   Given:  hdl-utils has been setup for project
    When:  User creates local.py file in directory containing VHDL files
     And:  User executes hdl-utils
    Then:  hdl-utils reads local.py file
     And:  hdl-utils applies properties

hdl-utils searches for directories with __init__.py files
---------------------------------------------------------

.. code-block:: gherkin

   Given:  __init__.py files have been added to project
    When:  

hdl-utils updates __init__.py files with HDL file information
-------------------------------------------------------------
