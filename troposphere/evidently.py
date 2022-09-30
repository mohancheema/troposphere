# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class MetricGoalObject(AWSProperty):
    """
    `MetricGoalObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html>`__
    """

    props: PropsDictType = {
        "DesiredChange": (str, True),
        "EntityIdKey": (str, True),
        "EventPattern": (str, True),
        "MetricName": (str, True),
        "UnitLabel": (str, False),
        "ValueKey": (str, True),
    }


class TreatmentToWeight(AWSProperty):
    """
    `TreatmentToWeight <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html>`__
    """

    props: PropsDictType = {
        "SplitWeight": (integer, True),
        "Treatment": (str, True),
    }


class OnlineAbConfigObject(AWSProperty):
    """
    `OnlineAbConfigObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html>`__
    """

    props: PropsDictType = {
        "ControlTreatmentName": (str, False),
        "TreatmentWeights": ([TreatmentToWeight], False),
    }


class RunningStatusObject(AWSProperty):
    """
    `RunningStatusObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html>`__
    """

    props: PropsDictType = {
        "AnalysisCompleteTime": (str, False),
        "DesiredState": (str, False),
        "Reason": (str, False),
        "Status": (str, False),
    }


class TreatmentObject(AWSProperty):
    """
    `TreatmentObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Feature": (str, True),
        "TreatmentName": (str, True),
        "Variation": (str, True),
    }


class Experiment(AWSObject):
    """
    `Experiment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html>`__
    """

    resource_type = "AWS::Evidently::Experiment"

    props: PropsDictType = {
        "Description": (str, False),
        "MetricGoals": ([MetricGoalObject], True),
        "Name": (str, True),
        "OnlineAbConfig": (OnlineAbConfigObject, True),
        "Project": (str, True),
        "RandomizationSalt": (str, False),
        "RemoveSegment": (boolean, False),
        "RunningStatus": (RunningStatusObject, False),
        "SamplingRate": (integer, False),
        "Segment": (str, False),
        "Tags": (Tags, False),
        "Treatments": ([TreatmentObject], True),
    }


class EntityOverride(AWSProperty):
    """
    `EntityOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html>`__
    """

    props: PropsDictType = {
        "EntityId": (str, False),
        "Variation": (str, False),
    }


class VariationObject(AWSProperty):
    """
    `VariationObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html>`__
    """

    props: PropsDictType = {
        "BooleanValue": (boolean, False),
        "DoubleValue": (double, False),
        "LongValue": (double, False),
        "StringValue": (str, False),
        "VariationName": (str, False),
    }


class Feature(AWSObject):
    """
    `Feature <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html>`__
    """

    resource_type = "AWS::Evidently::Feature"

    props: PropsDictType = {
        "DefaultVariation": (str, False),
        "Description": (str, False),
        "EntityOverrides": ([EntityOverride], False),
        "EvaluationStrategy": (str, False),
        "Name": (str, True),
        "Project": (str, True),
        "Tags": (Tags, False),
        "Variations": ([VariationObject], True),
    }


class ExecutionStatusObject(AWSProperty):
    """
    `ExecutionStatusObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html>`__
    """

    props: PropsDictType = {
        "DesiredState": (str, False),
        "Reason": (str, False),
        "Status": (str, True),
    }


class LaunchGroupObject(AWSProperty):
    """
    `LaunchGroupObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Feature": (str, True),
        "GroupName": (str, True),
        "Variation": (str, True),
    }


class MetricDefinitionObject(AWSProperty):
    """
    `MetricDefinitionObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html>`__
    """

    props: PropsDictType = {
        "EntityIdKey": (str, True),
        "EventPattern": (str, True),
        "MetricName": (str, True),
        "UnitLabel": (str, False),
        "ValueKey": (str, True),
    }


class GroupToWeight(AWSProperty):
    """
    `GroupToWeight <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html>`__
    """

    props: PropsDictType = {
        "GroupName": (str, True),
        "SplitWeight": (integer, True),
    }


class SegmentOverride(AWSProperty):
    """
    `SegmentOverride <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html>`__
    """

    props: PropsDictType = {
        "EvaluationOrder": (integer, True),
        "Segment": (str, True),
        "Weights": ([GroupToWeight], True),
    }


class StepConfig(AWSProperty):
    """
    `StepConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html>`__
    """

    props: PropsDictType = {
        "GroupWeights": ([GroupToWeight], True),
        "SegmentOverrides": ([SegmentOverride], False),
        "StartTime": (str, True),
    }


class Launch(AWSObject):
    """
    `Launch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html>`__
    """

    resource_type = "AWS::Evidently::Launch"

    props: PropsDictType = {
        "Description": (str, False),
        "ExecutionStatus": (ExecutionStatusObject, False),
        "Groups": ([LaunchGroupObject], True),
        "MetricMonitors": ([MetricDefinitionObject], False),
        "Name": (str, True),
        "Project": (str, True),
        "RandomizationSalt": (str, False),
        "ScheduledSplitsConfig": ([StepConfig], True),
        "Tags": (Tags, False),
    }


class AppConfigResourceObject(AWSProperty):
    """
    `AppConfigResourceObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html>`__
    """

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "EnvironmentId": (str, True),
    }


class S3Destination(AWSProperty):
    """
    `S3Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "Prefix": (str, False),
    }


class DataDeliveryObject(AWSProperty):
    """
    `DataDeliveryObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html>`__
    """

    props: PropsDictType = {
        "LogGroup": (str, False),
        "S3": (S3Destination, False),
    }


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html>`__
    """

    resource_type = "AWS::Evidently::Project"

    props: PropsDictType = {
        "AppConfigResource": (AppConfigResourceObject, False),
        "DataDelivery": (DataDeliveryObject, False),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Segment(AWSObject):
    """
    `Segment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html>`__
    """

    resource_type = "AWS::Evidently::Segment"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Pattern": (str, False),
        "Tags": (Tags, False),
    }
