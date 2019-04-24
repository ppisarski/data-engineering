# Data Engineering with Apache Airflow

## Installation

Install Airflow by running `pip install apache-airflow`.
Note, Airflow used to be packaged as `airflow` but since version 1.8.1 is packaged as `apache-airflow`.

## Running Airflow

Before you can use Airflow you have to initialize its database.
The database contains information about historical and current workflows, 
connections to external data sources, etc.
Once the database is setup Airflow UI can be accessed and workflows can be started.

The default database is SQLite, which is fine to start with.
In production setting use MySQL or PostgreSQL.
Airflow uses `AIRFLOW_HOME` environment variable to point to the location of
configuration files and SQLite database. 
By default Airflow creates directory `~/airflow/` to put the files in.

Next, initialize the database `airflow initdb`
and start the web server `airflow webserver --port 8080`.

Workflows can be started from a new terminal window.
`airflow run example_bash_operator runme_0 2017-07-01`

## Workflows

Create a workflow in Python by specifying actions as Directed Acyclic Graph (DAG).
Simplest DAG consist of the following tasks:
- print 'hello'
- wait 5 seconds
- print 'world'
Also lets plan daily execution of this workflow. 

### Create DAG file

Go to the Airflow home `cd $AIRFLOW_HOME` and find dags directory `dags/`.
Copy `tutoral.py` file that contains the DAG there.
The workflow will automatically be picked up and scheduled to run.

### Test the DAG

Check that DAG file contains valid Python code by executing `python tutorial.py`.
Manually test a single task for a given execution_date with `airflow test airflow_tutorial_v01 print_world 2017-07-01`.

### Activate the DAG

You need to turn the scheduler on with `airflow scheduler`.
In the list of DAGs with an on/off switch next to it you should see `airflow_tutorial_v01`.

## Resources
- Posts by Robert Chang
    - [A Beginner’s Guide to Data Engineering — Part I](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-i-4227c5c457d7)
    - [A Beginner’s Guide to Data Engineering — Part II](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-ii-47c4e7cbda71)
    - [A Beginner’s Guide to Data Engineering — The Series Finale](https://medium.com/@rchang/a-beginners-guide-to-data-engineering-the-series-finale-2cc92ff14b0)
- [Apache Airflow Tutorial for Data Pipelines](https://blog.godatadriven.com/practical-airflow-tutorial)
or [git repo](https://github.com/hgrif/airflow-tutorial)
- [Airflow documentation](https://airflow.apache.org/index.html)
- [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/)
- [Airflow: Tips, Tricks, and Pitfalls](https://medium.com/handy-tech/airflow-tips-tricks-and-pitfalls-9ba53fba14eb)
