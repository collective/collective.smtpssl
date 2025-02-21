.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.smtpssl/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.smtpssl/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.smtpssl/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.smtpssl?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.smtpssl/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.smtpssl

.. image:: https://img.shields.io/pypi/v/collective.smtpssl.svg
    :target: https://pypi.python.org/pypi/collective.smtpssl/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.smtpssl.svg
    :target: https://pypi.python.org/pypi/collective.smtpssl
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.smtpssl.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.smtpssl.svg
    :target: https://pypi.python.org/pypi/collective.smtpssl/
    :alt: License


==================
collective.smtpssl
==================

.. container:: del

    Patches zope.sendmail.mailer.SMTPMailer to use smtplib.SMTP_SSL instead of smtplib.SMTP, to support sending oder port 465.
    Please note, sending over port 587 will not work anymore when this package is installed!
    This is only necessary until is fixed.

    !! Note !! this is only working and useful for zope.sendmail < 6.2.
    From version 6.2 you can set implicit_tls to archive the same.


From version 2.0 on we don't patch the MailHost but enable the implicit_tls in the MailHost, so that one can use port 465.
This could be done in any setuphandlers.py, which would make this package obsolute in that setup.

Installation
------------

Install collective.smtpssl by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.smtpssl


and then running ``bin/buildout``


Authors
-------

Provided by Maik Derstappen | MrTango | derico.de


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.smtpssl/issues
- Source Code: https://github.com/collective/collective.smtpssl


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the GPLv2.
