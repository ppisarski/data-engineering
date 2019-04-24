# Apache Spark

1. Download Spark from [here](https://spark.apache.org/downloads.html).
2. Go to `spark/conf` directory and create config files
    - `cp slaves.template slaves` and modify as needed
    - `cp spark-env.sh.template spark-env.sh` and modify as needed
3. Launch Spark `sbin/start-all.sh`
4. Run jobs
5. You can monitor the cluster at https://localhost:8080 unless you changed something in the config files
6. When finished stop Spark `sbin/stop-all.sh`

