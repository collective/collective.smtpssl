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

Patches zope.sendmail.mailer.SMTPMailer to use smtplib.SMTP_SSL instead of smtplib.SMTP, to support sending oder port 465.

Features
--------

- Can be bullet points


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


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

Provided by awesome people ;)


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.smtpssl/issues
- Source Code: https://github.com/collective/collective.smtpssl
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
