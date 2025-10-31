from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, rank, dense_rank, desc, month, year, to_date,lag,row_number
from pyspark.sql.window import Window

def entry_point():
    spark=SparkSession.builder.getOrCreate()
    data = [
        ("E1", "Sales", "2025-01-05", 100),
        ("E1", "Sales", "2025-01-10", 200),
        ("E1", "Sales", "2025-02-15", 150),
        ("E1", "Sales", "2025-03-05", 300),
        ("E1", "Sales", "2024-12-25", 400),

        ("E2", "HR", "2025-01-10", 500),
        ("E2", "HR", "2025-02-20", 200),
        ("E2", "HR", "2025-03-10", 100),
        ("E2", "HR", "2024-11-11", 600),

        ("E3", "IT", "2025-01-15", 250),
        ("E3", "IT", "2025-02-10", 300),
        ("E3", "IT", "2024-12-30", 400)
    ]

    columns = ["emp_id", "department", "sale_date", "amount"]
    df=spark.createDataFrame(data,columns)
    df = df.withColumn("sale_date", to_date(col("sale_date")))
    df = df.withColumn("month", month(col("sale_date")))
    df = df.withColumn("year", year(col("sale_date")))
    source_df=df.orderBy("emp_id","year","month")
    source_df.show()

if __name__ == "__main__":
    entry_point()
