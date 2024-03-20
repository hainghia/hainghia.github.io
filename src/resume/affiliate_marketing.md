# Affiliate marketing

> #### PERMATE GLOBAL JOINT STOCK COMPANY
> *Lot 05 – 06 Area 2 Nguyen Sinh Sac, Hoa Minh, Lien Chieu, Da Nang, Viet Nam*
> ##### March 2023 - Present
---

## Situation:

During my tenure at a product company specializing in affiliate marketing, I was involved in building a network platform
for affiliate marketing.

## Task:

My responsibilities included tackling various challenges related to tracking, such as efficiently collecting a large
volume of traffic within a short timeframe using streaming technologies like Kinesis and Kafka. Additionally, I
addressed issues related to concurrency and high availability, optimizing data writing processes for big data into the
data lake. Moreover, I handled ETL processes, processing data from the data lake and pushing it to the data warehouse to
improve speed and performance for user reporting.

## Action:

To address tracking challenges, I utilized Chalice to construct Lambda functions to establish connection points and
collect data, which were then pushed to Kinesis. Subsequently, I employed Lambda as a consumer to receive data from
Kinesis events and push raw data to S3. From S3 (datalake), I utilized various technologies for ETL processes and moved
the data to the data warehouse to enable user reporting. Using Databricks, I utilized Delta Live Tables to partition the
data into separate components following the medallion architecture database model. Once the data was sufficiently
segmented, I loaded it back into RDS for querying and obtaining results.

In complex scenarios requiring computational capabilities and optimal performance, I turned to Snowflake. Here, I
leveraged Snowpipe to load data from previously stored S3 data. I used dynamic tables combined with medallion
architecture database principles to compute affiliate report metrics. Subsequently, I utilized Snowflake API to upload
the results for user querying.

## Result:

In earlier stages of the project, I initially utilized Glue and Redshift for ETL processes from S3. However, due to
performance issues, I transitioned to Databricks and Snowflake, resulting in improved efficiency and effectiveness.

Additionally, within this project, I provided guidance on microservice architecture and led team members in
collaborative development efforts.

By effectively utilizing a combination of technologies and methodologies, I successfully contributed to the development
and optimization of the affiliate marketing network platform.