==============
 About Colony
==============

This bugtracker was written in the intention to be a helpful tool.

Motivation
==========

* Fast (UI is fast, it's possible to use it very fast through the
  keyboard)

* well documented (zope, ncurses)


Running
=======

The project uses zc.buildout and a lot of zope components. Therefore you
do the following:

    * Use your python to do a bootstrap: python bootstrap.py
      It is recommended to use your own installed Python, rather than a
      system or distribution Python.

    * Do a buildout: bin/buildout
      This installs all the dependencies.

    * bin/colony runs the program.


Why the name 'Colony'?
======================

From wikipedia:

    Colony (biology), a group of individual organisms of the same
    species living closely together.
    http://en.wikipedia.org/wiki/Colony_(biology)

Because *one* bug tracker is used by *many* users (of the same company),
this bug tracker provides an application for *one* user tracking *many*
bug trackers. Therefore it deals with bugs from different systems,
providing a basis for 'living closely together.
