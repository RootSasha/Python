import boto3

# З'єднання з Amazon S3
aws_access_key_id = "You access key"
aws_secret_access_key = "You secret key"
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='eu-north-1')

# Створення нового відерка
bucket_name = 'You backet name'
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'})

# Виведення списку відер
response = s3.list_buckets()
bucket_list = [bucket['Name'] for bucket in response['Buckets']]
print(bucket_list)

# Завантаження файлів до відра
object_name1 = "file1.txt"
object_name2 = "file2.txt"
file_path1 = "C:\\Users\\sasha\\Desktop\\ШАГ\\Python\\3\\file1.txt"
file_path2 = "C:\\Users\\sasha\\Desktop\\ШАГ\\Python\\3\\file2.txt"

s3.upload_file(file_path1, bucket_name, object_name1)
s3.upload_file(file_path2, bucket_name, object_name2)
