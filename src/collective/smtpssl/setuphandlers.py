# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.smtpssl:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["collective.smtpssl.upgrades"]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.

    mail_host = api.portal.get_tool(name="MailHost")
    mail_host.manage_makeChanges(
        mail_host.title, mail_host.smtp_host, mail_host.smtp_port, implicit_tls=True
    )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
