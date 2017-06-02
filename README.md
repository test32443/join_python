# join_python
This is a sample project containing scripts to perform mapreduce join and aggregation using Python

To test without Hadoop:
cat customers.csv sales.csv  | ./mapper.py  | sort | ./reducer.py

To run in Hadoop:
hadoop jar /contrib/streaming/hadoop-streaming.jar -D mapred.reduce.tasks=1 -file ./mapper.py -mapper mapper.py -file ./reducer.py -reducer reducer.py -input customers.csv -input sales.csv -output result.csv -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf stream.map.output.field.separator=, -jobconf stream.num.map.output.key.fields=3 -jobconf map.output.key.field.separator=, -jobconf num.key.fields.for.partition=1
