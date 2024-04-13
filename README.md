# Simple OVOS Texting Skill

In order to enable SMS ability, you need a cellular module. So far this skill works with Waveshare's SIM7600X HAT. This is a skill rather than a plugin because of it simple task to only text one phone number. Also, you need to define the word "emergency" as one of OVOS's hotword.

```
"hotwords":{
        "Emergency":{
                "module":"ovos-ww-plugin-vosk",
                "samples":["emergency"],
                 "lang": "en",
                "rule":"fuzzy",
                "listen":false,
                "active":true,
                "bus_event":"text.emergency"
        }
    }
```

## About

The skill send a text to a phone number when the user says the word emergency.

## Credits
- Michelle Tran
- Mike Gray's skill generator - https://github.com/mikejgray/ovos-skill-projen
