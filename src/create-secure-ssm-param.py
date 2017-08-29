def lambda_handler(event, context):
    # TODO implement
    import boto3
    #import cfnresponse
    ssm = boto3.client('ssm')
    ssm.put_parameter
    if event['request'] == 'delete':
        try:
            ssm.delete_parameter(
                    Name=event['name']
                )
            print(f"deleted parameter: {event['name']}")
        except Exception as e: 
            if 'ParameterNotFound'  in str(e):
                print(f"tried to delete parameter: {event['name']} but it did not exist")
            else:
                raise Exception(f"unable to delete parameter: {event['name']}. error:" + str(e))
    else:
        try:
            ssm.put_parameter(
                    Name=event['name'],
                    Description=event['description'],
                    Value=event['value'],
                    Type='SecureString',
                    Overwrite=True
                )
            print(f"created secure parameter: {event['name']}")
        except Exception as e:
            raise Exception(f"unable to create parameter: {event['name']}. error:" + str(e))