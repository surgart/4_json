# Prettify JSON

The purpose of the pprint_json module is prettifying json data and print it into console. 

# Quickstart
To get an example of json file click this link:

https://devman.org/media/filer_public/1d/32/1d32132e-efa4-4a6c-bd32-312acc3710ad/alco_shops.json

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

```
An example of output:
```json

{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "DatasetId": 1854,
                "VersionNumber": 1,
                "ReleaseNumber": 2,
                "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
                "Attributes": {
                    "global_id": 14371450,
                    "Name": "Ароматный Мир",
                    "IsNetObject": "да",
                    "OperatingCompany": "Ароматный Мир",
                    "TypeService": "реализация продовольственных товаров",
                    "AdmArea": "Западный административный округ",
                    "District": "район Кунцево",
                    "Address": "улица Академика Павлова, дом 10",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ],
                    "WorkingHours": [
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "понедельник"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "вторник"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "среда"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "четверг"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "пятница"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "суббота"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "воскресенье"
                        }
                    ],
                    "ClarificationOfWorkingHours": null
                }
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
