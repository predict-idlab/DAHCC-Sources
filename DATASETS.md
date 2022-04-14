
An overview of all DAHCC datasets are provided here.

## DAHCC Protego

To accurately assess a call made for help by the person at home, it is important to get a good view of the daily activities and lifestyle of the person being monitored at home. Therefore, one of the aims within the [PROTEGO](https://www.imec-int.com/en/research-portfolio/protego)  project was to design algorithms that are able to automatically determine the activity/lifestyle of the monitored person based on the available sensor data in their home, e.g. sensors for location, movement, light, temperature, the use of certain devices, etc. or on the monitored people themselves, e.g. wearables or sensors on smartphone. In addition, a limited number of sensors are also provided for the monitored person to assess their condition, e.g. blood pressure or weight. The data collection is performed in the [c](https://www.ugent.be/ea/idlab/en/research/research-infrastructure/homelab.htm).

*Two protocols were performed with the study participants, namely a “day in the life” protocol and a “night” protocol. Each protocol starts with the same intake of the participant, which is performed by a researcher of IDLab. Each protocol also ends with the same outtake of the participant performed by a researcher of IDLab.*

In total: 31 "day in life" participants and 12 "night" participants enrolled in this protego study

### Homelab
The IDLab [HomeLab](https://idlab.technology/infrastructure/homelab/) was used for this study. The HomeLab is an 'ordinary' house on the UGent Campus Zwijnaarde, which is equipped with all kinds of sensors and actuators. It allows to test smart home applications in a very realistic environment.

The following rooms were used in the house by the participants:
-   Entry hallway
-   Toilet on the ground floor
-   Living room & Kitchen (1 big room)
-   Stairs to first floor
-   Bathroom on the first floor
-   Master bedroom on the first floor
-   Hallway on the first floor
-   Toilet on the first floor
    
After intake, the garage/office space was used by the supervising IDLAB researcher during the data collection (to not disturb the data collection).

The other rooms in the house were closed off (locked) such that the participants cannot enter them.

**A semantic description of the IDLab HomeLab, describing all the rooms and available sensors based on the DAHCC ontology is made available [here](https://raw.githubusercontent.com/predict-idlab/DAHCC-Ontology/main/instantiated_examples/_Homelab.owl)**

### Contextual sensors

Below a list of contextual sensors is given that are installed in the HomeLab and will be used within PROTEGO. These sensors were integrated using the [DYAMAND](https://dyamand.tech/) platform (except for the water running sensor which streams its data through the streaming application, see the section below). This platform collects the data from these sensors and provides it in a unified format.

| Measured parameter                                                           | Type of Sensor(s)                                            |
|------------------------------------------------------------------------------|--------------------------------------------------------------|
| Blood pressure                                                               | AnD UB-1100BLE                                               |
| Weight                                                                       | AnD UC-350BLE                                                |
| Body temperature                                                             | AnD UT-201BLE-A                                              |
| SpO2                                                                         | Nonin 3230                                                   |
| CO2                                                                          | Netatmo, Velbus (CO2)                                        |
| (Number of) persons detection in the rooms                                   | Steinel                                                      |
| Using doors, windows, cupboards & appliances in the home                     | EnOcean door-contact sensor                                  |
| Using lights in the home                                                     | Velbus + EnOcean                                             |
| Temperature inside in the house                                              | Velbus, Netatmo                                              |
| Use of door bell                                                             | Velbus                                                       |
| Detecting motion in the home/rooms                                           | PIR sensor through Velbus                                    |
| Opening & closing blinds                                                     | Velbus                                                       |
| Use of appliances plugged into sockets                                       | Velbus                                                       |
| Indicating sitting on the couch, lying on the couch, sitting at table, etc.  | EnOcean buttons pressed                                      |
| Localization of participants in the home using RF                            | Televic AQURA system                                         |
| Weather outside                                                              | Velbus weather station                                       |
| Water running                                                                | Self-constructed sensor on the faucets in bathroom & kitchen |
| AtmosphericPressure                                                          | Netatmo                                                      |
| Loudness                                                                     | Netatmo                                                      |

Some impressions of these sensors installed in the Homelab can be seen in the pictures below.  
  

![](https://lh6.googleusercontent.com/TsnPQVc1W048Eh6TzcwmiWGNfdIHIiIsbiMMfxtTuESWdygQJRjQDi---t2Q3pcYRUZ0wGOg-HZMsEcB1mZMa8oL48RX7PczkQOQFGchp87k1t4u4AcT5qSTEd6Un_E_lfKLcSkE)

Medical sensors in het upstairs bedroom

![](https://lh5.googleusercontent.com/KxaclzQYu7Eg_64w_z2sSwxbuH3qDigf8z4hV-klT6qjYLnQlSKXeqe9EBeWvxkm9qBp8Jn-LbRa2mniWwEnwmM6my1sH9o_Q4wZXtkplj_yDLrbEL9k4uKHa699Vuo3W1NSaTNY)

Steinel installed in the upstairs bedroom

![](https://lh5.googleusercontent.com/KRL4c-QZGwzvwyGDQeQbvPC6xFYb1R64fKM_nedT_S-k9b7U7yERaKh2w591wLlCA8V8CXvZDYp2JfB-WHf3Jh_j9xhBq0BTa8iXofMO567UBoyjjtzQjRS44DvOEE3ejjLNU1cr)

Netatmo installed in the downstairs toilet

![](https://lh3.googleusercontent.com/oWNRlfH1WC49PsGLPjdRkNtTwUACPQ8HuLW_s2G1eM3guQMtqH-Y0ewu5AHHMDfQuvWxo3-sVhNauur0zlIeAYWSZ8X-3llNzY2ka_YWAa1HBnmS387slHGb01dY186JwaOOAveV)

Netatmos and door contact sensors in the kitchen

![](https://lh5.googleusercontent.com/42com90Dsbm2_cF1DJW6DI5javE_T2aU_ydYS7R8Vx3g3rg4xg0lwq7sL14eGTN60wBlnnZ1bIOZpg9Hwpyov_IAVGnTUL0_nKxuJlxB2oZycEdX4Ymb34wC8Spn_POJ4_4TyS1a)

Participant wearing the AQURA bracelet & Empatica

![](https://lh6.googleusercontent.com/QVJhLysM4HpAtpuDhteo5hZWeWBcW3_89iTunUzw8CKe7zkuVwY4gtNpL5PYy7ovH-T49Dg4sK9u07INxztyq0A2emjExNy8SQg8XP9HUTtRK5rAY2Pr5G1Sd48gfqXSS_NEAh_y)  

Water Running Sensor

### Wearable & smartphone sensors and applications

Each participant was asked to install two smartphone applications: (a) the streaming application to collect data from the wearable (Empatica E4) and the smartphone sensors and send it to the data platform, and (b) the Sleep as Android application. The applications are only available for Android phones. If the participant does not have an Android phone, one will be provided by the researchers.

#### Empatica E4

The e4 wristband from [Empatica](https://www.empatica.com/research/e4/) is a wearable wireless band, which measures acceleration (x,y,z) (at 32 Hz), skin temperature (at 4 Hz), galvanic skin response (at 4 Hz), and blood volume pulse (at 64 Hz) (from which heart rate (variability) and the “inter beat interval” of the heart rate can be derived). The data of the wearable is streamed in real-time to the data platform by using Bluetooth and a streaming application on the smartphone (see below). The E4 is a CE medical certified device.

#### Streaming application & smartphone sensor data collection

The streaming application is an Android application that is installed on the smartphone of the participant if he/she has an Android phone or that is included on the smartphone provided to the participants that do not own an Android phone. Once the streaming application is configured by the researchers at the start of the data collection protocol, the participants only need to minimally interact with the application, namely only to check whether the data collection is still performing correctly or to reconnect the Empatica when Bluetooth connection is lost.

  
The streaming application is used for (a) streaming the data from the Empatica to the data platform, (b) collecting smartphone sensor data and sending it to the data platform
  

![](https://lh3.googleusercontent.com/0LRQ3jNKfs5Kt8N8GE1-rohn9pqOXsx59PKUdjcej-VKDpHTPXKe-ckSNkjaH7Hit7YfQREmguhO2NZqr_-8HLh6LaArbbI71Zg5Xgl9QjKdyFZFL2H52vKVBGt2j8s3KfSf-KTq)![](https://lh5.googleusercontent.com/ffdDN5C-1vk2PeoOIopYEx7SX54zWFCYWGiIaM_rMbIYx1cwnvdbMTScq54jb_eujRMNN5lXo6WYIUr5oK7pkJn0xJrR3mqbdtfnTVtkcRy3EFKScXZ-zltPHwuklDeoPszKGxS_)  
  
Concerning the smartphone the following data is collected: location of the smartphone (GPS coordinates), light intensity of the environment of the phone, frequency & amplitude of the noise in the environment measured through the smartphone microphone, acceleration of the smartphone, linear acceleration of the smartphone, values measured by the gyroscope in the smartphone, rotation of the smartphone, gravity applied to the smartphone, strength of the magnetic field around the smartphone, proximity of objects, applications opened by the user on the smartphone, timestamps of interaction with the keyboard of the smartphone by the user (only timestamp, NOT what was typed), adjustments to the status of the screen of the smartphone (on, off, locked, unlocked), number of steps performed by the participant, and the probable start and stop time of the sleep period of the participant (performed with the [Google Sleep API](https://developers.google.com/location-context/sleep)). Some parameters can only be performed by Android phones that have the necessary sensors available and when the smartphone’s operating system is up-to-date.

#### Sleep as Android application

The participants will also install the [Sleep as Android](https://sleep.urbandroid.org/) application (or it is installed on the provided phone). When sleeping with the smartphone in the bed, based on the phone’s sensors the application will perform sleep cycle tracking, collect snoring stats, collect room noise stats and start sleep and awake detection. The application Sleep as Android is only used in Off-line mode. As such, it only collects data on the smartphone of the participant itself (if he/she is using his/her own smartphone) or on the IDLab phone. At the end of the data collection, the participant sends a ZIP file of the collected data to the supervising researcher. The researcher places the ZIP of the secure IDLab Cloud environment.

#### Web application for activity annotation

A web application was designed by IDLab that allows participants to (a) enter the activities they perform as part of routine, (b) indicate when they start/stop such an activity.

This was used during the data collection to allow participants to annotate the actions they are performing. For usability purposes, we wrapped this web application inside an android app and ensured that a preloaded set of activities and routines could be loaded from either a prefilled CSV file or directly from the google cloud. Everytime a participant interacted with the application (when the start, end or cancel button was pressed), a timestamp together with the performed action was sent to a log file corresponding to the participants name. This log file was later on analysed to derive the annotations. Participants were also able to insert new activities using a text field in the protego annotator. They could also log some additional information, such as unexpected application crashes, or problems with some of the appliances inside the homelab.

  
![](https://lh4.googleusercontent.com/xsMMihGrMlHP4jgxX-LwyzY9aO7wh3mkXP-ConYbfEgTCsJnq2MXmnR-_z-C8L0v1WDQFo_A-w_MgsrF4lmFlIvGybRdRUcnY2HlvzpsvplvaauaRuQ9eliGAjeFD14bxq0QJCpv)  ![](https://lh3.googleusercontent.com/PP0nVscaBMZ-91Zy7_CNaC0MkdtmTRae_9gw0zEWnG2hMyWnI8kB5eVilzd_hxKzYFAaW1GqJ5yFRtDdS2eaARpclQgcKOsRZzK8V_yKbe2fG4N8GYgxfMbnQWzINy5lmzN-tGvn)



### Raw Dataset

[Full Protego Day Dataset](https://dahcc.idlab.ugent.be/data/protego_day.tar.gz) - 22G

| user          | data                                                                              | labels                                                                          |
|---------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| participant_1 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant1/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant1/labels.csv) |
| participant_2 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant2/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant2/labels.csv) |
| participant_3 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant3/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant3/labels.csv) |
| participant_4 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant4/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant4/labels.csv) |
| participant_5 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant5/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant5/labels.csv) |
| participant_6 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant6/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant6/labels.csv) |
| participant_7 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant7/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant7/labels.csv) |
| participant_8 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant8/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant8/labels.csv) |
| participant_9 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant9/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant9/labels.csv) |
| participant_10 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant10/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant10/labels.csv) |
| participant_11 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant11/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant11/labels.csv) |
| participant_12 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant12/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant12/labels.csv) |
| participant_13 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant13/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant13/labels.csv) |
| participant_14 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant14/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant14/labels.csv) |
| participant_15 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant15/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant15/labels.csv) |
| participant_16 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant16/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant16/labels.csv) |
| participant_17 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant17/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant17/labels.csv) |
| participant_18 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant18/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant18/labels.csv) |
| participant_19 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant19/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant19/labels.csv) |
| participant_20 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant20/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant20/labels.csv) |
| participant_21 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant21/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant21/labels.csv) |
| participant_22 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant22/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant22/labels.csv) |
| participant_23 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant23/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant23/labels.csv) |
| participant_24 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant24/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant24/labels.csv) |
| participant_25 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant25/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant25/labels.csv) |
| participant_26 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant26/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant26/labels.csv) |
| participant_27 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant27/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant27/labels.csv) |
| participant_28 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant28/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant28/labels.csv) |
| participant_29 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant29/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant29/labels.csv) |
| participant_30 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant30/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant30/labels.csv) |
| participant_31 | [data.feather](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant31/data.feather) | [labels.csv](https://dahcc.idlab.ugent.be/data/Protego_anom/_participant31/labels.csv) |
