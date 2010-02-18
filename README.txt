=====================
 About Superorganism
=====================

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
