#  Ec2-launch-event-detection

## Overview
It will detect the Ec2 launch and sent a alert to slack/teams.

Template is written based on AWS Serverless Model Applicaiton Specification.

[AWS SAM Template Concepts](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-basics.html)

## Resources
- Lambda Function
- Lambda Role
- Event Bridge
- Event Bridge
- Statemachine
- Statemachine
## Deployment
```
aws cloudformation package --template-file remediate-public-facing-sg.yaml --s3-bucket <Deployment S3 Bucket Name > --output-template-file packaged-template.yaml 

aws cloudformation deploy --template-file packaged-template.yaml --stack-name ec2-launch-event-dectection 

```
Where Deployment S3 Bucket Name is the bucket to upload the CFn template and lambda code. Can be any bucket current or new.
