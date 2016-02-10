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


class ConstantProduct(Model):
    """
    The product documentation.

    :param str const_property: Constant string. Default value: "constant" .
    :param str const_property2: Constant string2. Default value: "constant2" .
    """

    _required = ['const_property', 'const_property2']

    _attribute_map = {
        'const_property': {'key': 'constProperty', 'type': 'str'},
        'const_property2': {'key': 'constProperty2', 'type': 'str'},
    }

    def __init__(self, *args, **kwargs):
        self.const_property = None
        self.const_property2 = None

        super(ConstantProduct, self).__init__(*args, **kwargs)