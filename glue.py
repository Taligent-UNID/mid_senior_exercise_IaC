import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": False,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://target-tali/db/clientes/"], "recurse": True},
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Amazon S3
AmazonS3_node1676274827082 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": False,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://target-tali/db/ventas/"], "recurse": True},
    transformation_ctx="AmazonS3_node1676274827082",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("col0", "string", "ID", "int"),
        ("col1", "string", "Cliente", "string"),
        ("col2", "string", "Tipo", "string"),
        ("col3", "string", "Telefono", "string"),
        ("col4", "string", "Ubicacion", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Change Schema (Apply Mapping)
ChangeSchemaApplyMapping_node1676274856719 = ApplyMapping.apply(
    frame=AmazonS3_node1676274827082,
    mappings=[
        ("col1", "string", "NFactura", "string"),
        ("col2", "string", "Fecha", "string"),
        ("col3", "string", "Cliente", "string"),
        ("col4", "string", "MontoSinImp", "string"),
        ("col5", "string", "Impuestos", "string"),
        ("col6", "string", "MontoFactura", "string"),
    ],
    transformation_ctx="ChangeSchemaApplyMapping_node1676274856719",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://transformed-tali/clientes/", "partitionKeys": []},
    transformation_ctx="S3bucket_node3",
)

# Script generated for node Amazon S3
AmazonS3_node1676274864696 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchemaApplyMapping_node1676274856719,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://transformed-tali/ventas/", "partitionKeys": []},
    transformation_ctx="AmazonS3_node1676274864696",
)

job.commit()
