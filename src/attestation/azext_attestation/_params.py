# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    resource_group_name_type,
)


def load_arguments(self, _):

    with self.argument_context('attestation create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='Name of the attestation service')
        c.argument('attestation_policy', id_part=None, help='Name of attestation policy.')
        c.argument('policy_signing_certificates', id_part=None, help='JSON Web Key Set defining a set of X.509 Certificates that will represent the parent certificate for the signing certificate used for policy operations')

    with self.argument_context('attestation update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='Name of the attestation service')
        c.argument('attestation_policy', id_part=None, help='Name of attestation policy.')
        c.argument('policy_signing_certificates', id_part=None, help='JSON Web Key Set defining a set of X.509 Certificates that will represent the parent certificate for the signing certificate used for policy operations')

    with self.argument_context('attestation delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='Name of the attestation service')

    with self.argument_context('attestation show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='Name of the attestation service')