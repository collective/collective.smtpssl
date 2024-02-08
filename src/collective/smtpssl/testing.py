# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.smtpssl


class CollectiveSmtpsslLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.smtpssl)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.smtpssl:default')


COLLECTIVE_SMTPSSL_FIXTURE = CollectiveSmtpsslLayer()


COLLECTIVE_SMTPSSL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SMTPSSL_FIXTURE,),
    name='CollectiveSmtpsslLayer:IntegrationTesting',
)


COLLECTIVE_SMTPSSL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SMTPSSL_FIXTURE,),
    name='CollectiveSmtpsslLayer:FunctionalTesting',
)


COLLECTIVE_SMTPSSL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SMTPSSL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveSmtpsslLayer:AcceptanceTesting',
)
