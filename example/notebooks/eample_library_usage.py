# Databricks notebook source
# MAGIC %md # Runner

# COMMAND ----------

df = spark.read.csv("/video_games.csv").select("*").toPandas()

# COMMAND ----------

from example_library import example_library

example_library.get_game_by_name("Super Mario 64 DS", df).display()
