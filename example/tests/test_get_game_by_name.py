from example_library import example_library
import unittest
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


class get_game_by_name_tests(unittest.TestCase):
    # Load csv file from remote DataBricks file storage
    def mock_gamedata_df(self):
        return spark.read.csv("/video_games.csv").select("*").toPandas()

    # Test that the returned DataFrame has the right value(s)
    def test_get_game_by_name_returns_expected_df(self):
        df = example_library.get_game_by_name(
                "Super Mario 64 DS",
                get_game_by_name_tests.mock_gamedata_df(self))
        self.assertEqual(df['_c0'].values,'Super Mario 64 DS')

    # Test that the returned DataFrame is empty when called with bad value
    def test_get_game_by_name_returns_empty_df(self):
        df = example_library.get_game_by_name(
                "Not A Vaild Game Name",
                get_game_by_name_tests.mock_gamedata_df(self))
        self.assertTrue(df.empty)
