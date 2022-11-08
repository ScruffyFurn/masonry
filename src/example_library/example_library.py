from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)


class example_library:
    # Get a game from dataframe based on name
    def get_game_by_name(gameName, dataset):
        """Get Game By Name"""
        # column "_c0" is the name column in the video game dataset
        df = dataset.query(f'_c0 == "{gameName}"'.format(gameName))
        if df.any:
            return df
        else:
            return df.empty
