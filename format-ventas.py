from datetime import date
import boto3
s3 = boto3.client('s3')
data = s3.get_object(Bucket='target-tali', Key='db/ventas/LOAD00000001.csv')
file_lines = data['Body'].iter_lines()
transformedData = []
for i in file_lines:
    i = i[1:-2]
    i = i.replace(' $', '')
    i = i.replace(' "', '"')
    i = i.replace(' ",', '",')
    i = i.split(',')
    d = i[1]
    d = d.split("/")
    d = str(date(int(d[2]), int(d[1]), int(d[0])))
    i[1] = d
    i = ",".join(str(e) for e in i)
    transformedData.append(i)
with open('ventas-test.csv', 'w') as file:
    for i in transformedData:
        file.write(i)
s3.meta.client.upload_file('ventas.csv', 'target-tali', 'db/ventas/formatted/ventas.csv')