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


class ValidateContainerSettingsRequest(Model):
    """Container settings validation request context.

    :param base_url: Base URL of the container registry
    :type base_url: str
    :param username: Username for to access the container registry
    :type username: str
    :param password: Password for to access the container registry
    :type password: str
    :param repository: Repository name (image name)
    :type repository: str
    :param tag: Image tag
    :type tag: str
    :param platform: Platform (windows or linux)
    :type platform: str
    """

    _attribute_map = {
        'base_url': {'key': 'baseUrl', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ValidateContainerSettingsRequest, self).__init__(**kwargs)
        self.base_url = kwargs.get('base_url', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.repository = kwargs.get('repository', None)
        self.tag = kwargs.get('tag', None)
        self.platform = kwargs.get('platform', None)
