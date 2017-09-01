# to do:
# function to handle cfnresponse
# decide if an rds parameter should be overwritten (or be given a unique name?)
import boto3
import cfnresponse
ssm = boto3.client('ssm')
def create_ssm_secure_parameter(Name,Description,Value):
    try:
        ssm.put_parameter(
                Name=Name,
                Description=Description,
                Value=Value,
                Type='SecureString',
                Overwrite=True
            )
        print(f"created secure ssm parameter: \"{Name}\"")
    except Exception as e:
        raise Exception(f"unable to create parameter: \"{Name}\". error:" + str(e))

def delete_ssm_parameter(Name):
    try:
        ssm.delete_parameter(Name=Name)
        print(f"deleted parameter: {Name}")
    except Exception as e: 
        if 'ParameterNotFound' in str(e):
            print(f"called delete_parameter for \"{Name}\", but the ssm parameter does not exist")
        else:
            raise Exception(f"unable to delete parameter \"{Name}\". error:" + str(e))
            
def lambda_handler(event, context):
    print(f"received event: {event}")
    params = event['ResourceProperties']
    try:
        if event['RequestType'] == 'Delete':
            delete_ssm_parameter(params['Name'])
        else:
            create_ssm_secure_parameter(params['Name'],params['Description'],params['Value'])
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    except Exception as e:
        cfnresponse.send(event, context, cfnresponse.FAILED, {}) 