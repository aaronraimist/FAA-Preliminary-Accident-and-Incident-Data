# FAA Preliminary Accident and Incident Data
The Federal Aviation Administration publishes [Preliminary Accident and Incident Reports](https://www.asias.faa.gov/apex/f?p=100:93:::NO:::) but this data is only visible for the preceding 10 days. After that it cannot be retrieved from the FAA until the [Aviation Accident and Incident Database](https://www.asias.faa.gov/apex/f?p=100:12:::NO:::) is updated which can take a year or two. Sometimes it is useful to be able to lookup the FAA preliminary report for an incident in the span of time where it is not visible on the FAA's website. This repository contains the FAA's accident/incident data going back to August 10th 2021 and data will be retained indefinitely.

Note that this is mostly only useful for [*incidents*](https://www.law.cornell.edu/cfr/text/49/830.2). The National Transportation Safety Board investigates all [aviation *accidents*](https://www.law.cornell.edu/cfr/text/49/830.2). The NTSB usually produces a much more detailed preliminary report within a few weeks following the accident and a final report within a year or two. NTSB reports can be obtained using the [CAROL Query tool](https://data.ntsb.gov/carol-main-public/basic-search).

This data comes directly from the FAA and has not been cleaned. There is known bad data in here such dates from the future and impossible timestamps like 00:90:00Z.