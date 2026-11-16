"""Assignment 4 - Spark program: number of products sold in each caliber.

Usage: python sales_by_caliber.py [path/to/sales.csv]
Input columns: sale_id, product, caliber, quantity, price
"""
import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

path = sys.argv[1] if len(sys.argv) > 1 else "data/sales.csv"

spark = SparkSession.builder.appName("SalesByCaliber").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

sales = spark.read.csv(path, header=True, inferSchema=True)

result = (
    sales.groupBy("caliber")
    .agg(
        F.sum("quantity").alias("products_sold"),
        F.count("*").alias("num_sales"),
    )
    .orderBy(F.desc("products_sold"))
)
result.show()

# Same answer with Spark SQL
sales.createOrReplaceTempView("sales")
spark.sql(
    "SELECT caliber, SUM(quantity) AS products_sold FROM sales "
    "GROUP BY caliber ORDER BY products_sold DESC"
).show()

spark.stop()
