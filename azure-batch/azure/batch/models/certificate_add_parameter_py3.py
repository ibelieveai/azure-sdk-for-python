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


class CertificateAddParameter(Model):
    """A certificate that can be installed on compute nodes and can be used to
    authenticate operations on the machine.

    All required parameters must be populated in order to send to Azure.

    :param thumbprint: Required. The X.509 thumbprint of the certificate. This
     is a sequence of up to 40 hex digits (it may include spaces but these are
     removed).
    :type thumbprint: str
    :param thumbprint_algorithm: Required. The algorithm used to derive the
     thumbprint. This must be sha1.
    :type thumbprint_algorithm: str
    :param data: Required. The base64-encoded contents of the certificate. The
     maximum size is 10KB.
    :type data: str
    :param certificate_format: The format of the certificate data. Possible
     values include: 'pfx', 'cer'
    :type certificate_format: str or ~azure.batch.models.CertificateFormat
    :param password: The password to access the certificate's private key.
     This is required if the certificate format is pfx. It should be omitted if
     the certificate format is cer.
    :type password: str
    """

    _validation = {
        'thumbprint': {'required': True},
        'thumbprint_algorithm': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'thumbprint_algorithm': {'key': 'thumbprintAlgorithm', 'type': 'str'},
        'data': {'key': 'data', 'type': 'str'},
        'certificate_format': {'key': 'certificateFormat', 'type': 'CertificateFormat'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, *, thumbprint: str, thumbprint_algorithm: str, data: str, certificate_format=None, password: str=None, **kwargs) -> None:
        super(CertificateAddParameter, self).__init__(**kwargs)
        self.thumbprint = thumbprint
        self.thumbprint_algorithm = thumbprint_algorithm
        self.data = data
        self.certificate_format = certificate_format
        self.password = password