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


class TimeZoneTimeZoneInformation(Model):
    """Defines a date and time for a geographical location.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The name of the geographical location.For
     example, County; City; City, State; City, State, Country; or Time Zone.
    :type location: str
    :param time: Required. The data and time specified in the form,
     YYYY-MM-DDThh;mm:ss.ssssssZ.
    :type time: str
    :param utc_offset: Required. The offset from UTC. For example, UTC-7.
    :type utc_offset: str
    """

    _validation = {
        'location': {'required': True},
        'time': {'required': True},
        'utc_offset': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'time': {'key': 'time', 'type': 'str'},
        'utc_offset': {'key': 'utcOffset', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TimeZoneTimeZoneInformation, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.time = kwargs.get('time', None)
        self.utc_offset = kwargs.get('utc_offset', None)
