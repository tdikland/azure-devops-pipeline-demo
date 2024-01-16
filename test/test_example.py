import pytest

import pyspark.testing
from pyspark.testing.utils import assertDataFrameEqual

def test_it_works():
    assert 1 == 1

def test_another():
    assert True

def test_more():
    assert 2 + 2 == 4

def test_f(spark_fixture):
    df_in = spark_fixture.read.csv("/Users/Tim.Dikland/customers/sse/azure-devops-pipeline-demo/test/fixtures/names.csv", header=True)
    df_in.show()
    assert 0

