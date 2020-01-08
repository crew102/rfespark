import pyspark

spark = pyspark.sql.SparkSession.builder.appName('test').getOrCreate()


def test_spark():
    x = spark.range(10).collect()
    assert len(x) == 10
