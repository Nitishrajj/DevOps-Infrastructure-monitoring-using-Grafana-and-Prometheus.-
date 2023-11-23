# DevOps-Infrastructure-monitoring-using-Grafana-and-Prometheus.-

This project centers around establishing a robust and comprehensive infrastructure monitoring system using Grafana and Prometheus within a DevOps environment. The primary focus is on monitoring the nodes within the infrastructure to ensure optimal performance, identify potential issues, and facilitate timely responses to maintain system health.
Also the project places a particular emphasis on monitoring individual nodes within the infrastructure. Metrics related to CPU usage, memory consumption, disk I/O, network activity, and other node-specific indicators are collected and visualized.

# Getting started 
Tools used 
Grafana -- 
Grafana serves as the visualization and dashboarding platform, providing an intuitive and customizable interface for monitoring and analyzing data.
Dashboards are crafted to offer a real-time, consolidated view of critical metrics, empowering DevOps teams to make informed decisions promptly.
The monitoring solution is designed to be scalable, accommodating the growth of the infrastructure. Grafana's flexibility ensures adaptability to diverse infrastructure setups, making it suitable for both small-scale and large-scale deployments.

Prometheus -- 
Prometheus acts as the core monitoring and alerting component, responsible for collecting and storing time-series data from various nodes in the infrastructure.
Customizable Prometheus queries enable the extraction of relevant metrics, empowering operators to gain insights into resource utilization, system performance, and potential bottlenecks.

# Implementation 
We have implemented this project using the help of above tools. So basically we started to first install node exporter into the nodes (n number of nodes here). We have used jenkins (CI/CD tool) to install and run node exporter in the pipeline. 
So, then we have hosted prometheus and grafana and started collecting metrics using node exporter to prometheus. As, prometheus doesn't have any type of visualization Grafana has so we are using this same prometheus as the data source for our grafana dashboard. Now the grafana dashboard is set. We can also set alerts to the dashboard and integrate in different ways. 
