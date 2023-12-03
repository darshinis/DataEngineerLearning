##############################################################################################
"""
Step :
1. create sparSession : spark = SparkSession.builder.master("local[*]").getOrCreate() - entry point for spark applications
2. create sparkContext : sc = spark.sparkContext - used to create RDD from values and files
"""
##############################################################################################
#                                       step 1                                               #
##############################################################################################
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext
##############################################################################################
#                        Step : reading csv from git - commad : !wget                        #
##############################################################################################
df = spark.read.csv("cars.csv",header = True,sep=";")
df = spark.read.format("csv")\ # type of file
                .option("header"=True)\ # ("inferschema" : True), .schema("schema string")
                .option("delimiter"=";)\
                .option("mode"="PERMISSIVE")\ # (mode : PERMISSIVE,DROPMALFORMED,FAILFAST)
                .load("cars.csv")
##############################################################################################
#                                different actions on Data Frame                             #
##############################################################################################
"""
1. count
2. reduce
3. reduceByKey
4. take
5. first
6. SaveTextFile : save the RDD file has partitions
7. reduceByKey
"""
#############################################################################################
#                                      Transformation                                       #
#############################################################################################



