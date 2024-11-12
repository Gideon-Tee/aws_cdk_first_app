from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_ecr as ecr,
)


class MyFirstCdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "MyFirstCdkAppQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "MyFirstCdkAppTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))



        # L1
        cfn_repository = ecr.CfnRepository(
            self,
            "RepoL1",
            image_scanning_configuration=ecr.CfnRepository.ImageScanningConfigurationProperty(
                scan_on_push=False
            ),
            repository_name="repo-l1"
        )

        # L2
        repository = ecr.Repository(self, "repo-l2")
