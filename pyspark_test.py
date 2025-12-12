from pyspark.sql import SparkSession from pyspark.sql.
functions import col, lit, row_
number from pyspark.sql.
window import Window # Initialize Spark session spark = SparkSession
.builder.app
Name("EWM_MD
M_STAGE_FACI
LITY").getOr
Create() # Database connection parameters db_
url = "jdbc:oracle
:thin:@hostn
ame:port/ser
vice_name" db_propertie
s = { "user": "username", "password": "password", "driver": "oracle.jdbc
driver.Orac
leDriver" } # Dynamic parameters selection_da
te = '20230101' # Example date, should be dynamically set src_
dl_
value = 'SRC_DL_VALU
E' # Example SRC_
DL value, should be dynamically set # Read data from Oracle tables try: df_EWM_MDM_S
TAGE_FCY_AR_
IP_JDCL_EV = spark.read.f
ormat("jdbc"
).options( url=db_
url, dbtable="EWM
_MDM_STAGE_F
CY_AR_IP_JDC
L", user=db_prop
erties["user
"], password=db_
properties["
password"]