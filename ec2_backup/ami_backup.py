
#!/usr/bin/env python3
import boto3
import datetime

print ("hello world")
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    now = datetime.datetime.now()
    
    # Create a new AMI
    response = ec2.create_image(
        InstanceId='i-0c696286c9a30e840',  # Replace with your instance ID
        Name=f'timsamanchi-Backup-AMI-{now.strftime("%Y-%m-%d-%H-%M-%S")}',
        Description='tim samanchi - Automated backup test',
        NoReboot=True
    )
    
    # Delete old AMIs based on retention criteria
    retention_days = 7  # Adjust retention days as needed
    
    images = ec2.describe_images(Filters=[{'Name': 'tag:Name', 'Values': ['Backup-AMI-*']}])
    for image in images['Images']:
        creation_date = image['CreationDate']
        image_id = image['ImageId']
        age = (now - datetime.datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S.%fZ")).days
        
        if age >= retention_days:
            ec2.deregister_image(ImageId=image_id)
            print(f'Deleted old AMI: {image_id}')
    
    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully'
    }
