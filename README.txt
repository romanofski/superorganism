=====================
 About Superorganism
=====================

This bugtracker is a prototype of a decentralised bug tracking system.
See the functional specification for more information.

Hacking
=======

If you would like to hack on the project, please follow the coding
style:

    * follow PEP8: http://www.python.org/dev/peps/pep-0008/
    * always absolute imports, sorted by the first module name
    * try to test your code as good as possible
    * the commit messages follow the GNOME guidelines:
      http://live.gnome.org/Git/CommitMessages

Please read the functional specification in the "doc" directory.


Why should I use Superorganism?
===============================

    * you already have to use a bug tracker which lacks of functionality
    * you need something small for your own (private) development
    * you work on many different projects, but need an overview of all
      outstanding tasks/bugs

I can't see any value in using Superorganism, if you already use a very
good bug tracking system. At least not from now ...


Used Technology
---------------

I decided to use the following components:

    * urwid - for the UI. Most of the content in bug tracking systems we
      deal with is text. A text-based application if well implemented,
      can provide a fast and usable UI for developers.
    * zope.component - for glueing the components together. One of the
      goals of this bug tracking system is to be highly extensible. The
      component architecture can provide the glue for creating a highly
      extensible system.
    * ZODB - Currently the best choice for storing objects.


License
=======

I'm currently distributing the project under GPL v3. See COPYING.

* most of the content which is managed by every common bug tracker is:
  text


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

I have to admit, that the name may change in the future. I'm not quite
convinced if it's a good name. I was also considering:

    * colony
    * magpie
