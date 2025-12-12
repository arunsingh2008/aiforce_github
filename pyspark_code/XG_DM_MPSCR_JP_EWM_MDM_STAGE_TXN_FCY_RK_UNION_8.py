from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, to_date
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# Initialize Spark session
spark = SparkSession.builder 
    .appName("DataStage to PySpark") 
    .getOrCreate()

# Read data from EWM_MDM_STAGE_TXN_FCY_RK_MASTER
df_master = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//hostname:port/service",
    dbtable="EWM_MDM_STAGE_TXN_FCY_RK_MASTER",
    user="username",
    password="password"
).load().select(
    "EV_ID",
    "MSTR_SRC_STM_CD",
    "MSTR_SRC_STM_KEY",
    "VLD_FROM_TMS",
    "VLD_TO_TMS",
    "PRIM_AR_ID",
    "FCY_RK",
    "TXN_BOOK_DT",
    "TXN_CCY_AMT",
    "TXN_CCY_CL_CD",
    "TXN_RSN_TP_CL_CD",
    "LDGR_CCY_AMT",
    "LDGR_CCY_CL_CD",
    "SRC_DL",
    "DATA_DT"
).where(
    (col("SRC_DL") == "DL_DE") & (col("DATA_DT") == to_date("20240516", "yyyyMMdd"))
)

# Read data from EWM_MDM_STAGE_TXN_FCY_RK_DIRECT
df_direct = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//hostname:port/service",
    dbtable="EWM_MDM_STAGE_TXN_FCY_RK_DIRECT",
    user="username",
    password="password"
).load().select(
    "EV_ID",
    "MSTR_SRC_STM_CD",
    "MSTR_SRC_STM_KEY",
    "VLD_FROM_TMS",
    "VLD_TO_TMS",
    "PRIM_AR_ID",
    "FCY_RK",
    "TXN_BOOK_DT",
    "TXN_CCY_AMT",
    "TXN_CCY_CL_CD",
    "TXN_RSN_TP_CL_CD",
    "LDGR_CCY_AMT",
    "LDGR_CCY_CL_CD",
    "SRC_DL",
    "DATA_DT"
).where(
    (col("SRC_DL") == "DL_DE") & (col("DATA_DT") == to_date("20240516", "yyyyMMdd"))
)

# Read data from EWM_MDM_STAGE_TXN_FCY_RK_AGRMT
df_agrmt = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//hostname:port/service",
    dbtable="EWM_MDM_STAGE_TXN_FCY_RK_AGRMT",
    user="username",
    password="password"
).load().select(
    "MSTR_SRC_STM_CD",
    "MSTR_SRC_STM_KEY",
    "VLD_FROM_TMS",
    "VLD_TO_TMS",
    "PRIM_AR_ID",
    "FCY_RK",
    "TXN_BOOK_DT",
    "TXN_CCY_AMT",
    "TXN_CCY_CL_CD",
    "TXN_RSN_TP_CL_CD",
    "LDGR_CCY_AMT",
    "LDGR_CCY_CL_CD",
    "SRC_DL",
    "DATA_DT"
).where(
    (col("SRC_DL") == "DL_DE") & (col("DATA_DT") == to_date("20240516", "yyyyMMdd"))
)

# Union the dataframes
df_union = df_master.union(df_direct).union(df_agrmt)

# Deduplicate the dataframe
window_spec = Window.partitionBy("PRIM_AR_ID", "FCY_RK", "SRC_DL", "MSTR_SRC_STM_KEY").orderBy("VLD_FROM_TMS")
df_dedup = df_union.withColumn("row_number", row_number().over(window_spec)).where(col("row_number") == 1).drop("row_number")

# Sort the dataframe
df_sorted = df_dedup.orderBy("SRC_DL", "PRIM_AR_ID", "FCY_RK", "VLD_FROM_TMS")

# Transform the dataframe
df_transformed = df_sorted.withColumn("SYS_INRT_TMS", current_timestamp())

# Write the dataframe to the target table
df_transformed.write.format("jdbc").options(
    url="jdbc:oracle:thin:@//hostname:port/service",
    dbtable="EWM_MDM_STAGE_TXN_FCY_RK_UNION",
    user="username",
    password="password"
).mode("append").save()

# Stop the Spark session
spark.stop()
