import pytest

import pyspark.testing
from pyspark.testing.utils import assertDataFrameEqual

from src.transform import cleanse_name_column

def test_cleanse_name_column(spark_fixture):
    # GIVEN
    df_in = spark_fixture.createDataFrame([(1, " Mark"), (2, "Lisa"), (3, "Sophie ")], "id INT, value STRING")
    df_out = spark_fixture.createDataFrame([(1, "Mark"), (2, "Lisa"), (3, "Sophie")], "id INT, name STRING")

    # WHEN
    df_transformed = df_in.transform(cleanse_name_column)

    # THEN
    assertDataFrameEqual(df_transformed, df_out)