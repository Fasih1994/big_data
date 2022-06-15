from paths import get_path

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]

def spark_job(spark,sc):
    sc.addPyFile(get_path(__file__))
    df = spark.createDataFrame(data=data, schema = columns)
    df.createOrReplaceTempView("PERSON_DATA")
    groupDF = spark.sql("SELECT gender, count(*) from PERSON_DATA group by gender")
    groupDF.show()