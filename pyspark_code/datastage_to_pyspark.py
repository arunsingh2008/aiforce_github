from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, current_timestamp
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# Initialize Spark session
spark = SparkSession.builder 
    .appName("DataStage to PySpark") 
    .getOrCreate()

# Read data from source tables
df_fcy_ar_ip_jdcl = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//<host>:<port>/<service>",
    dbtable="EWM_MDM_STAGE_FCY_AR_IP_JDCL",
    user="<user>",
    password="<password>"
).load().where("DATA_DT = TO_DATE('20221130','YYYYMMDD') AND SRC_DL = 'DL_IT'")

df_ar_x_ar_r = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//<host>:<port>/<service>",
    dbtable="EWM_AR_X_AR_R",
    user="<user>",
    password="<password>"
).load().where("SRC_DL='DL_IT' AND VLD_FROM_TMS<= TO_DATE('20221130235959' , 'YYYYMMDDHH24MISS') AND TO_DATE('20221130235959' , 'YYYYMMDDHH24MISS') < VLD_TO_TMS")

df_fcy_ar = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//<host>:<port>/<service>",
    dbtable="EWM_MDM_STAGE_FCY_AR",
    user="<user>",
    password="<password>"
).load().where("DATA_DT = TO_DATE('20221130','YYYYMMDD') AND SRC_DL = 'DL_IT'")

df_ar_identn_m = spark.read.format("jdbc").options(
    url="jdbc:oracle:thin:@//<host>:<port>/<service>",
    dbtable="EWM_AR_IDENTN_M",
    user="<user>",
    password="<password>"
).load().where("SRC_DL='DL_IT' AND VLD_FROM_TMS<= TO_DATE('20221130235959' , 'YYYYMMDDHH24MISS') AND TO_DATE('20221130235959' , 'YYYYMMDDHH24MISS') < VLD_TO_TMS AND AR_IDENTN_TP_CL_CD = 'LCL_VORTEX_IDENT'")

# Deduplicate EWM_MDM_STAGE_FCY_AR_IP_JDCL
window_spec = Window.partitionBy("SRC_DL", "AR_ID").orderBy("SRC_DL")
df_fcy_ar_ip_jdcl_dedup = df_fcy_ar_ip_jdcl.withColumn("row_number", row_number().over(window_spec)) 
    .where(col("row_number") == 1).drop("row_number")

# Perform joins
df_joined = df_fcy_ar_ip_jdcl_dedup 
    .join(df_ar_x_ar_r, ["SRC_DL", "AR_ID"], "left_outer") 
    .join(df_fcy_ar, ["SRC_DL", "AR_ID"], "left_outer") 
    .join(df_ar_identn_m, ["SRC_DL", "AR_ID"], "left_outer")

# Perform transformations
df_transformed = df_joined 
    .withColumn("DATE_FROM", col("mov_FCY_AR_IDENTN.SYS_VLD_FROM_TMS")) 
    .withColumn("DATE_TO", col("mov_FCY_AR_IDENTN.SYS_VLD_TO_TMS")) 
    .withColumn("HIGHER_FCY_RK", when(col("mov_FCY_AR_IDENTN.HIGHER_FCY_RK").isNull(), col("mov_FCY_AR_IDENTN.FCY_RK")).otherwise(col("mov_FCY_AR_IDENTN.HIGHER_FCY_RK"))) 
    .withColumn("HIGHEST_FCY_RK", when(col("mov_FCY_AR_IDENTN.HIGHEST_FCY_RK").isNull(), col("mov_FCY_AR_IDENTN.FCY_RK")).otherwise(col("mov_FCY_AR_IDENTN.HIGHEST_FCY_RK"))) 
    .withColumn("LOWEST_LVL_IND", when(col("mov_FCY_AR_IDENTN.HLEAF") == 1, lit("Y"))
                .when(col("mov_FCY_AR_IDENTN.HLEAF") == 0, lit("N"))
                .when(col("mov_FCY_AR_IDENTN.HIGHEST_FCY_IN_HRY") == "Y", lit("N"))
                .otherwise(lit("Y"))) 
    .withColumn("FCY_VORTEX_ID", col("mov_FCY_AR_IDENTN.AR_IDENTN_NM")) 
    .withColumn("SYS_INRT_TMS", current_timestamp())

# Write the transformed data to the target table
df_transformed.select(
    "DATA_DT",
    "FCY_ID",
    "SRC_STM_ID",
    "DATE_FROM",
    "AR_ID",
    "DATE_TO",
    "SRC_DL",
    "FCY_RK",
    "FCY_AR_TP",
    "HIGHER_FCY_RK",
    "HIGHEST_FCY_RK",
    "LOWEST_LVL_IND",
    "SPSDG_FCY_RK",
    "COURT_CTRLD_WRKOUT_FILL_DT",
    "COURT_CTRLD_WRKOUT_FCY",
    "OUT_OF_COURT_WRKOUT_FCY",
    "SPSDG_FCY_DT",
    "COURT_CTRLD_WRKOUT_CLS_DT",
    "CR_OBLG_DFLTD",
    "FCY_VORTEX_ID",
    "SYS_INRT_TMS"
).write.format("jdbc").options(
    url="jdbc:oracle:thin:@//<host>:<port>/<service>",
    dbtable="EWM_MDM_STAGE_FACILITY",
    user="<user>",
    password="<password>"
).mode("append").save()

# Stop the Spark session
spark.stop()
