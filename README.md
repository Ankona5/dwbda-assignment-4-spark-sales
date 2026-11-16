# Assignment 4 – Spark: products sold in each caliber

**Name:** Ankona Mukherjee
**Registration No.:** 202400560

## Task
Take the sales data and write a Spark program to calculate the number of products sold in each caliber.

## Files
| File | Purpose |
|---|---|
| `sales_by_caliber.py` | PySpark program (DataFrame API and Spark SQL versions) |
| `data/sales.csv` | Sample sales data (500 generated rows: `sale_id, product, caliber, quantity, price`) |

The data is generated sample data, not real sales records. To use your own, keep the same columns.

## Run
```bash
pip install pyspark
python sales_by_caliber.py            # uses data/sales.csv
python sales_by_caliber.py my.csv     # or your own file
```

## Output
```
+-----------+-------------+---------+
|    caliber|products_sold|num_sales|
+-----------+-------------+---------+
|      Small|         1936|      185|
|     Medium|         1684|      150|
|      Large|         1095|      102|
|Extra Large|          667|       63|
+-----------+-------------+---------+
```
