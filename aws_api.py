import boto3

region="us-east-1"
_ec = boto3.client('ec2',region_name=region)
instances= _ec.describe_instances()
print(instances)