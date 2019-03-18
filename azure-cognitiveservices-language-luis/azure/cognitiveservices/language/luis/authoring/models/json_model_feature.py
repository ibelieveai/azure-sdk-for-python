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


class JSONModelFeature(Model):
    """Exported Model - Phraselist Model Feature.

    :param activated: Indicates if the feature is enabled.
    :type activated: bool
    :param name: The Phraselist name.
    :type name: str
    :param words: List of comma-separated phrases that represent the
     Phraselist.
    :type words: str
    :param mode: An interchangeable phrase list feature serves as a list of
     synonyms for training. A non-exchangeable phrase list serves as separate
     features for training. So, if your non-interchangable phrase list contains
     5 phrases, they will be mapped to 5 separate features. You can think of
     the non-interchangeable phrase list as an additional bag of words to add
     to LUIS existing vocabulary features. It is used as a lexicon lookup
     feature where its value is 1 if the lexicon contains a given word or 0 if
     it doesn’t.  Default value is true.
    :type mode: bool
    """

    _attribute_map = {
        'activated': {'key': 'activated', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'words': {'key': 'words', 'type': 'str'},
        'mode': {'key': 'mode', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(JSONModelFeature, self).__init__(**kwargs)
        self.activated = kwargs.get('activated', None)
        self.name = kwargs.get('name', None)
        self.words = kwargs.get('words', None)
        self.mode = kwargs.get('mode', None)
