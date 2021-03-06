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


class DataConnectionValidationResult(Model):
    """The result returned from a data connection validation request.

    :param error_message: A message which indicates a problem in data
     connection validation.
    :type error_message: str
    """

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataConnectionValidationResult, self).__init__(**kwargs)
        self.error_message = kwargs.get('error_message', None)
