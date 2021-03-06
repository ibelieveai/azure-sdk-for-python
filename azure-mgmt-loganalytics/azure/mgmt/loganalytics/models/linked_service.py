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

from .proxy_resource import ProxyResource


class LinkedService(ProxyResource):
    """The top level Linked service resource container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param resource_id: Required. The resource id of the resource that will be
     linked to the workspace.
    :type resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LinkedService, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)
