from time import sleep
from pyspark.sql import SparkSession
from pi import calculate_pi
from job1 import spark_job
import os
from threading import Thread

def multiple_jobs(spark,sc):
    p1 = Thread(target=calculate_pi, args=(sc, 2))
    p1.start()
    print('calculate pi started')

    p2 = Thread(target=spark_job, args=(spark, sc))
    print("Job 1 started")
    p2.start()

if __name__=="__main__":
    print("trying to start spark")

    spark = SparkSession.builder.master('local[*]').appName("PythonPi").getOrCreate()
    sc = spark.sparkContext
    sc.addPyFile(os.getcwd()+'/spark_jobs/paths.py')
    multiple_jobs(spark,sc)
    sleep(30)
    spark.stop()