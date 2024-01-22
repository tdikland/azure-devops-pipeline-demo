import pytest

from pyspark.sql import SparkSession

import os

from warnings import filterwarnings

filterwarnings(
    "ignore", message="distutils Version classes are deprecated. Use packaging.version instead."
)

os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"


@pytest.fixture
def spark_fixture():
    spark = SparkSession.builder.getOrCreate()
    yield spark