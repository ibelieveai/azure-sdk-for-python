# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Peering(Model):
    """Peering is a logical representation of a set of connections to the
    Microsoft Cloud Edge at a location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param sku: Required. The SKU that defines the tier and kind of the
     peering.
    :type sku: ~azure.mgmt.peering.models.PeeringSku
    :param direct: The properties that define a direct peering.
    :type direct: ~azure.mgmt.peering.models.PeeringPropertiesDirect
    :param exchange: The properties that define an exchange peering.
    :type exchange: ~azure.mgmt.peering.models.PeeringPropertiesExchange
    :param peering_location: The location of the peering.
    :type peering_location: str
    :ivar provisioning_state: The provisioning state of the resource. Possible
     values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.peering.models.ProvisioningState
    :param location: Required. The location of the resource.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'sku': {'required': True},
        'provisioning_state': {'readonly': True},
        'location': {'required': True},
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'PeeringSku'},
        'direct': {'key': 'properties.direct', 'type': 'PeeringPropertiesDirect'},
        'exchange': {'key': 'properties.exchange', 'type': 'PeeringPropertiesExchange'},
        'peering_location': {'key': 'properties.peeringLocation', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Peering, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.direct = kwargs.get('direct', None)
        self.exchange = kwargs.get('exchange', None)
        self.peering_location = kwargs.get('peering_location', None)
        self.provisioning_state = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.name = None
        self.id = None
        self.type = None
        self.kind = None
