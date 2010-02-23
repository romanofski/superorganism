=====================
 About Superorganism
=====================

This bugtracker is a prototype of a decentralised bug tracking system.
See the functional specification for more information.

Hacking
=======

If you would like to hack on the project, please follow the coding
style:

    * follow PEP8
    * always absolute imports, sorted by the first module name
    * try to test your code as good as possible

Running
=======

Dependencies to other software packages are mostly resolved
automatically, but obviously you need Python (2.5 recommended).

The project uses zc.buildout and a lot of zope components. Therefore you
do the following:

    * Use your python to do a bootstrap: python bootstrap.py
      It is recommended to use your own installed Python, rather than a
      system or distribution Python.

    * Do a buildout: bin/buildout
      This installs all the dependencies.

    * bin/superorganism runs the program.


Why the name 'Superorganism'?
==============================

From wikipedia:

    A superorganism is an organism consisting of many organisms. This is
    usually meant to be a social unit of eusocial animals, where
    division of labour is highly specialised and where individuals are
    not able to survive by themselves for extended periods of time.
    http://en.wikipedia.org/wiki/Superorganism

Because *one* bug tracker is used by *many* users (of the same company),
this bug tracker provides an application for *one* user tracking *many*
bug trackers. Therefore it deals with bugs from different systems,
providing a basis for 'living closely together.
