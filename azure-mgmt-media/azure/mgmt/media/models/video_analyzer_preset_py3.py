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

from .audio_analyzer_preset_py3 import AudioAnalyzerPreset


class VideoAnalyzerPreset(AudioAnalyzerPreset):
    """A video analyzer preset that extracts insights (rich metadata) from both
    audio and video, and outputs a JSON format file.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param audio_language: The language for the audio payload in the input
     using the BCP-47 format of 'language tag-region' (e.g: 'en-US'). The list
     of supported languages are, 'en-US', 'en-GB', 'es-ES', 'es-MX', 'fr-FR',
     'it-IT', 'ja-JP', 'pt-BR', 'zh-CN', 'de-DE', 'ar-EG', 'ru-RU', 'hi-IN'. If
     not specified, automatic language detection would be employed. This
     feature currently supports English, Chinese, French, German, Italian,
     Japanese, Spanish, Russian, and Portuguese. The automatic detection works
     best with audio recordings with clearly discernable speech. If automatic
     detection fails to find the language, transcription would fallback to
     English.
    :type audio_language: str
    :param insights_to_extract: The type of insights to be extracted. If not
     set then based on the content the type will selected.  If the content is
     audio only then only audio insights are extracted and if it is video only.
     Possible values include: 'AudioInsightsOnly', 'VideoInsightsOnly',
     'AllInsights'
    :type insights_to_extract: str or ~azure.mgmt.media.models.InsightsType
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'audio_language': {'key': 'audioLanguage', 'type': 'str'},
        'insights_to_extract': {'key': 'insightsToExtract', 'type': 'str'},
    }

    def __init__(self, *, audio_language: str=None, insights_to_extract=None, **kwargs) -> None:
        super(VideoAnalyzerPreset, self).__init__(audio_language=audio_language, **kwargs)
        self.insights_to_extract = insights_to_extract
        self.odatatype = '#Microsoft.Media.VideoAnalyzerPreset'