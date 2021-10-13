# FAA Preliminary Accident and Incident Data
The Federal Aviation Administration publishes [Preliminary Accident and Incident Reports](https://www.asias.faa.gov/apex/f?p=100:93:::NO:::) but this data is only visible for the preceding 10 days. After that it cannot be retrieved from the FAA until the [Aviation Accident and Incident Database](https://www.asias.faa.gov/apex/f?p=100:12:::NO:::) is updated which can take a year or two. Sometimes it is useful to be able to lookup the FAA preliminary report for an incident in the span of time where it is not visible on the FAA's website. This repository contains the FAA's accident/incident data going back to August 10th 2021 and data will be retained indefinitely.

Note that this is mostly only useful for [*incidents*](https://www.law.cornell.edu/cfr/text/49/830.2). The National Transportation Safety Board investigates all [aviation *accidents*](https://www.law.cornell.edu/cfr/text/49/830.2). The NTSB usually produces a much more detailed preliminary report within a few weeks following the accident and a final report within a year or two. NTSB reports can be obtained using the [CAROL Query tool](https://data.ntsb.gov/carol-main-public/basic-search).

## Example:

| UPDATED | ENTRY_DATE | EVENT_LCL_DATE | EVENT_LCL_TIME | LOC_CITY_NAME | LOC_STATE_NAME | LOC_CNTRY_NAME | RMK_TEXT                                                                    | EVENT_TYPE_DESC | FSDO_DESC            | REGIST_NBR | FLT_NBR | ACFT_OPRTR        | ACFT_MAKE_NAME | ACFT_MODEL_NAME | ACFT_MISSING_FLAG | ACFT_DMG_DESC | FLT_ACTIVITY | FLT_PHASE             | FAR_PART | MAX_INJ_LVL | FATAL_FLAG | FLT_CRW_INJ_NONE | FLT_CRW_INJ_MINOR | FLT_CRW_INJ_SERIOUS | FLT_CRW_INJ_FATAL | FLT_CRW_INJ_UNK | CBN_CRW_INJ_NONE | CBN_CRW_INJ_MINOR | CBN_CRW_INJ_SERIOUS | CBN_CRW_INJ_FATAL | CBN_CRW_INJ_UNK | PAX_INJ_NONE | PAX_INJ_MINOR | PAX_INJ_SERIOUS | PAX_INJ_FATAL | PAX_INJ_UNK | GRND_INJ_NONE | GRND_INJ_MINOR | GRND_INJ_SERIOUS | GRND_INJ_FATAL | GRND_INJ_UNK |
| ------- | ---------- | -------------- | -------------- | ------------- | -------------- | -------------- | --------------------------------------------------------------------------- | --------------- | -------------------- | ---------- | ------- | ----------------- | -------------- | --------------- | ----------------- | ------------- | ------------ | --------------------- | -------- | ----------- | ---------- | ---------------- | ----------------- | ------------------- | ----------------- | --------------- | ---------------- | ----------------- | ------------------- | ----------------- | --------------- | ------------ | ------------- | --------------- | ------------- | ----------- | ------------- | -------------- | ---------------- | -------------- | ------------ |
| No      | 04-OCT-21  | 01-OCT-21      | 18:45:00Z      | POTTSTOWN     | PENNSYLVANIA   | UNITED STATES  | AIRCRAFT GROUND LOOPED ON LANDING, POTTSTOWN, PA.                           | ACCIDENT        | ALLENTOWN FSDO       | N329CC     |         |                   | CULPS SPECIAL  | SOPWITH         | No                | SUBSTANTIAL   | PERSONAL     | LANDING (LDG)         | 91.0     | NONE        | No         | 1.0              | 0                 | 0                   | 0                 | 0.0             | 0                | 0                 | 0                   | 0                 | 0               | 0.0          | 0             | 0               | 0             | 0           | 0             | 0              | 0                | 0              | 0            |
| No      | 04-OCT-21  | 01-OCT-21      | 20:05:00Z      | PHILADELPHIA  | PENNSYLVANIA   | UNITED STATES  | AIRCRAFT STRUCK A BIRD DAMAGING #1 ENGINE, PHILADELPHIA, PA.                | INCIDENT        | PHILADELPHIA FSDO    | N917UY     | AAL2531 | AMERICAN AIRLINES | AIRBUS         | A321            | No                | MINOR         | COMMERCIAL   | TAKEOFF (TOF)         | 121.0    | NONE        | No         | 2.0              | 0                 | 0                   | 0                 | 0.0             | 4                | 0                 | 0                   | 0                 | 0               | 195.0        | 0             | 0               | 0             | 0           | 0             | 0              | 0                | 0              | 0            |
| No      | 04-OCT-21  | 01-OCT-21      | 21:30:00Z      | GRAND FORKS   | NORTH DAKOTA   | UNITED STATES  | AIRCRAFT DURING LANDING INCURRED A TAIL STRIKE, GRAND FORKS, ND.            | INCIDENT        | FARGO FSDO           | N770ND     |         |                   | PIPER          | PA28            | No                | UNKNOWN       | INSTRUCTION  | LANDING (LDG)         | 91.0     | NONE        | No         | 1.0              | 0                 | 0                   | 0                 | 0.0             | 0                | 0                 | 0                   | 0                 | 0               | 1.0          | 0             | 0               | 0             | 0           | 0             | 0              | 0                | 0              | 0            |
| No      | 04-OCT-21  | 01-OCT-21      | 23:25:00Z      | LOUISVILLE    | KENTUCKY       | UNITED STATES  | AIRCRAFT LANDED AND VEERED OFF RUNWAY INTO THE GRASS, LOUISVILLE, KY.       | INCIDENT        | LOUISVILLE FSDO      | N456SP     |         |                   | CESSN          | 172             | No                | UNKNOWN       | PERSONAL     | LANDING (LDG)         | 91.0     | UNKNOWN     | No         | 0.0              | 0                 | 0                   | 0                 | 1.0             | 0                | 0                 | 0                   | 0                 | 0               | 0.0          | 0             | 0               | 0             | 0           | 0             | 0              | 0                | 0              | 0            |
| No      | 04-OCT-21  | 02-OCT-21      | 01:30:00Z      | CHICAGO       | ILLINOIS       | UNITED STATES  | AIRCRAFT PULLING INTO GATE AND STRUCK THE WINGTIP OF RPA3594, CHICAGO, IL.  | INCIDENT        | GREATER CHICAGO FSDO | N141SY     | SKW5845 | SKYWEST AIRLINES  | EMBRAER        | ERJ170          | No                | MINOR         | COMMERCIAL   | PUSHBACK/TOWING (PBT) | 121.0    | NONE        | No         | 2.0              | 0                 | 0                   | 0                 | 0.0             | 2                | 0                 | 0                   | 0                 | 0               | 47.0         | 0             | 0               | 0             | 0           | 0             | 0              | 0                | 0              | 0            |
| No      | 04-OCT-21  | 02-OCT-21      | 01:30:00Z      | CHICAGO       | ILLINOIS       | UNITED STATES  | AIRCRAFT WAS PUSHING BACK FROM GATE AND WAS STRUCK BY SKW5845, CHICAGO, IL. | INCIDENT        | GREATER CHICAGO FSDO | N730YX     | RPA3594 | REPUBLIC AIRWAYS  | EMBRAER        | E175            | No                | MINOR         | COMMERCIAL   | PUSHBACK/TOWING (PBT) | 121.0    | NONE        | No         | 2.0              | 0                 | 0                   | 0                 | 0.0             | 2                | 0                 | 0                   | 0                 | 0               | 72.0         | 0             | 0               | 0             | 0           | 0             | 0              | 0                | 0              | 0            |

This data comes directly from the FAA and has not been cleaned. There is known bad data in here such dates from the future and impossible timestamps like 00:90:00Z.