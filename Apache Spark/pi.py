from random import random
import pyspark as ps

conf = ps.SparkConf()
conf.setAppName('Pi')
conf.setMaster('spark://localhost:7077')
sc = ps.SparkContext(conf=conf)


def inside(_):
    x, y = random(), random()
    return x * x + y * y <= 1


NUM_SAMPLES = 9999999999

count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
print("Pi is roughly {}".format(4.0 * count / NUM_SAMPLES))
