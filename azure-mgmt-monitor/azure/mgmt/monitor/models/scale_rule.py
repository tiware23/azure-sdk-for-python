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


class ScaleRule(Model):
    """A rule that provide the triggers and parameters for the scaling action.

    :param metric_trigger: the trigger that results in a scaling action.
    :type metric_trigger: :class:`MetricTrigger
     <azure.mgmt.monitor.models.MetricTrigger>`
    :param scale_action: the parameters for the scaling action.
    :type scale_action: :class:`ScaleAction
     <azure.mgmt.monitor.models.ScaleAction>`
    """ 

    _validation = {
        'scale_action': {'required': True},
    }

    _attribute_map = {
        'metric_trigger': {'key': 'metricTrigger', 'type': 'MetricTrigger'},
        'scale_action': {'key': 'scaleAction', 'type': 'ScaleAction'},
    }

    def __init__(self, scale_action, metric_trigger=None):
        self.metric_trigger = metric_trigger
        self.scale_action = scale_action
