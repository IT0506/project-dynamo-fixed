Read the Apache access log located at /app/access.log.



Generate a JSON report at exactly:



/app/report.json



The report must be a JSON object.



Success criteria:



1\. Write the output to /app/report.json.

2\. The output must be valid JSON.

3\. Include a field named total\_requests containing the total number of log entries.

4\. Include a field named unique\_ips containing the number of distinct client IP addresses.

5\. Include a field named top\_path containing the most frequently requested request path.

