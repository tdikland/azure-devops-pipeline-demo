import boto3

s3 = boto3.client("s3", aws_access_key_id="AKIAEXAMPLE", aws_secret_access_key="TEST")

url = s3.generate_presigned_url("get_object", Params={"Bucket": "bucket", "Key": "prefix/key.json"}, ExpiresIn=3600)

print(url)


print("hello world!")

