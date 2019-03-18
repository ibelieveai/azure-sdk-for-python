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


class ApplicationSettingUpdateObject(Model):
    """Object model for updating an application's settings.

    :param is_public: Setting your application as public allows other people
     to use your application's endpoint using their own keys.
    :type is_public: bool
    """

    _attribute_map = {
        'is_public': {'key': 'public', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ApplicationSettingUpdateObject, self).__init__(**kwargs)
        self.is_public = kwargs.get('is_public', None)
