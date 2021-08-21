from pyspark.sql import SparkSession
import pytest

@pytest.fixture(scope='module')
def spark():
    spark_session = SparkSession.builder.appName('LocalEnv').getOrCreate()
    yield spark_session
    spark_session = None


def test_spark_instance(spark):
    df = spark.read.csv('data/test_data.csv', header=True, inferSchema=True)
    #df.head(3)
    #print(df.columns)
    results = df.select('birth_year').head(20)
    for x in results:
        print(f'The birth year is: {x.birth_year}')