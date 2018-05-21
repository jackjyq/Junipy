# API Documentation :memo:
---
This documentation covers the coffe shop order web API.

#### Media Type support
---
All server response bodies and request bodies MUST be valid **[JSON](https://tools.ietf.org/search/rfc4627)** messages.

### Orders :coffee:
---
The **Orders** URL (/orders/) is the base URL for reading and updating Order objects The table below shows all the Task-related operations, their URLs, methods, and payloads.

#### Table 1. Homepage
|    Operation  | URL | Method | Returns | Inputs |
| ---------- | --------------- |---- |--- |--- |
| get GDP,flags | /home |GET |[GDP&Flags](#GDP&Flags) | None|


### Detail

The **Detail** URL (/detail/) is the base URL for get country detail objects and supports the following operations:

#### Table 2. country detail
|    Operation    | URL | Method | Returns | Inputs |
| ---------- | --------------- |---- |--- |--- |
|get the detail of the country | /detail/&lt;code&gt;/ |GET | [detail](#detail) |country code |


## Responses :eyes:
----
The home API returns payloads (as JSON object):
* [GDP&flags](#GDP&flags)
* [Detail](#Detail)

See below for details.

### <a name="GDP&flags"></a> GDP&flags Json
A **GDP&flags** looks like this:
```json
{
  "GDP": 
        {"AD": 2858517699.11504, 
        "AE": 348743265704.561, 
        "AF": 19469022207.6357...
        }, 
  "flags": 
        [
          {"name": "Afghanistan", "flag": "\ud83c\udde6\ud83c\uddeb", "code": "AF"},
          {"name": "Albania", "flag": "\ud83c\udde6\ud83c\uddf1", "code": "AL"},
          {"name": "Algeria", "flag": "\ud83c\udde9\ud83c\uddff", "code": "DZ"},...          
        ]
}
```


See **[Data Elements](#Data)** for more information on each property.

---

#### <a name="Detail"></a> Detail Json

A ** country detail** looks like this:
```json
{
    "name": "United States of America",
    "introduction": "Britain's American colonies broke with the mother country in 1776 and were recognized as the new nation of the United States of America following the Treaty of Paris in 1783. During the 19th and 20th centuries...",
    "flag": "https://www.cia.gov/library//publications/the-world-factbook/graphics/flags/large/us-lgflag.gif",
"GDPHistory": [
        {
            "year": "1990",
            "value": "5979589000000"
        },
        {
            "year": "1991",
            "value": "6174043000000"
        },
        {
            "year": "1992",
            "value": "6539299000000"
        }
        ...
    ],
     "agriculture": null,
     "agriculturePercent": null,
    "agricultureHistory": [
        {
            "year": "1990",
            "value": null
        },
        {
            "year": "1991",
            "value": null
        },
        {
            "year": "1992",
            "value": null
        },
        ...
    ],
    "industry": null,
    "industryPrecent": null,
    "industryHistory": [
        {
            "year": "1990",
            "value": null
        },
        {
            "year": "1991",
            "value": null
        },
        {
            "year": "1992",
            "value": null
        },
        ...
    ],
    "service": null,
    "servicePrecent": null,
    "serviceHistory": [
        {
            "year": "1990",
            "value": null
        },
        {
            "year": "1991",
            "value": null
        },
        {
            "year": "1992",
            "value": null
        },
        ...
    ],
    "CO2": null,
    "CO2History": [
        {
            "year": "1990",
            "value": "4823403.118"
        },
        {
            "year": "1991",
            "value": "4820847.219"
        },
        {
            "year": "1992",
            "value": "4909533.614"
        },
        ...
    ],
    "PM25Index": "9.19693412255931",
    "PM25IndexHistory": [
        {
            "year": "1990",
            "value": "11.3781550939233"
        },
        {
            "year": "1991",
            "value": null
        },
        {
            "year": "1992",
            "value": null
        },
       ...
    ],
    "freshwaterWithdrawals": null,
    "freshwaterWithdrawalsHistory": [
        {
            "year": "1990",
            "value": "465.1"
        },
        {
            "year": "1991",
            "value": null
        },
        {
            "year": "1992",
            "value": null
        },
        ...
    ]
}
```






## <a name="Data"></a> Data Elements :sushi:
---
There is all the parameters describtion

##### <a name="home"></a> home detail

|    Name  | Meaning | Type | Optional
| --- | --- | --- |:----:|
| GDP | [countrycode](#countryCode):latest year GDP | String:Int | :heavy_multiplication_x: |
| flags | name:full name, flag:emoij, code:countrycode| String:String | :heavy_multiplication_x: |


##### <a name="Detail"></a> country detail

|    Name  | Meaning | Type | Optional
| --- | --- | --- |:----:|
| name| country full name | String | :heavy_multiplication_x: |
| introduction | country's short introduction | String | :heavy_multiplication_x: |
| flag | URL of large flag picture | String | :heavy_multiplication_x:|
| GDP | latest year GDP | String |:heavy_multiplication_x: |
| GDPHistory | {year:,value:} | String:String | :heavy_multiplication_x: |
| agriculture | latest year agriculture | String |:heavy_multiplication_x: | 
| agriculturePrecent | latest year agriculture percentage | String |:heavy_multiplication_x: | 
| agricultureHistory | {year:,value:} | String:String | :heavy_multiplication_x: |
| industry | latest year industry | String |:heavy_multiplication_x: | 
| industryPrecent | latest year industry percentage | String |:heavy_multiplication_x: | 
| industryHistory | {year:,value:} | String:String | :heavy_multiplication_x: |
| service | latest year service | String |:heavy_multiplication_x: | 
| servicePrecent | latest year service percentage | String |:heavy_multiplication_x: | 
| serviceHistory | {year:,value:} | String:String | :heavy_multiplication_x: |
| CO2 | latest year CO2 emission | String |:heavy_multiplication_x: |
| CO2History | {year:,value:} | String:String | :heavy_multiplication_x: |
| PM25Index | latest year PM2.5 | String |:heavy_multiplication_x: |
| PM25IndexHistory | {year:,value:} | String:String | :heavy_multiplication_x: |
| freshwaterWithdrawals | latest year freshwaterWithdrawals | String |:heavy_multiplication_x: |
| GDPHistory | {year:,value:} | String:String | :heavy_multiplication_x: |
| population | latest year population | String |:heavy_multiplication_x: |
| populationHistory | {year:,value:} | String:String | :heavy_multiplication_x: |

#### <a name="countryCode"></a>  Country Code 
```json
	[
    {
        "name": "Afghanistan",
        "flag": "🇦🇫",
        "code": "AF",
        "dial_code": "+93"
    },
    {
        "name": "Åland Islands",
        "flag": "🇦🇽",
        "code": "AX",
        "dial_code": "+358"
    },
    {
        "name": "Albania",
        "flag": "🇦🇱",
        "code": "AL",
        "dial_code": "+355"
    },
    {
        "name": "Algeria",
        "flag": "🇩🇿",
        "code": "DZ",
        "dial_code": "+213"
    },
    {
        "name": "American Samoa",
        "flag": "🇦🇸",
        "code": "AS",
        "dial_code": "+1684"
    }
    ...
    ]
```




