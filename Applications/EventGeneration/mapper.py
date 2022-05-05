import sys
import logging
import pytz
from datetime import datetime

uuid_map = {}

# MAPPING FUNCTIONS OF HEADACHE PARTS
ACTIVITY_FIXED = """
<http://protego.idlab.imec.be/act%s> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://saref.etsi.org/saref4ehaw/Activity> ."""
ACTIVITY_TEMPLATE_TYPE = """
<http://protego.idlab.imec.be/act%s> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/%s> . """
ACTIVITY_TEMPLATE = """
<http://protego.idlab.imec.be/act%s> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/activityStart> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://protego.idlab.imec.be/act%s> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/activityEnd> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://protego.idlab.imec.be/usr%s> <https://saref.etsi.org/saref4ehaw/hasActivity> <http://protego.idlab.imec.be/act%s> ."""


PHONE_FIXED = """
<http://protego.idlab.imec.be/post%s> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://saref.etsi.org/saref4ehaw/Posture> ."""
PHONE_TEMPLATE_TYPE = """
<http://protego.idlab.imec.be/post%s> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/%s> .
<http://protego.idlab.imec.be/post%s> <http://www.w3.org/2000/01/rdf-schema#label> "%s" . """

PHONE_TEMPLATE = """
<http://protego.idlab.imec.be/post%s> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/activityStart> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://protego.idlab.imec.be/post%s> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/activityEnd> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://protego.idlab.imec.be/usr%s> <https://saref.etsi.org/saref4ehaw/hasPosture> <http://protego.idlab.imec.be/post%s> ."""

def generate_actid(patient_id):
    key = str("patient")
    if key not in uuid_map:
        uuid_map[key] = 0
    result = uuid_map[key]
    uuid_map[key] += 1
    return result

def map_activities(patient_id,activity, start, end):
    uuid = generate_actid(patient_id)
    str = ACTIVITY_FIXED % (uuid)
    for x in activity.split(', '):
        str+=ACTIVITY_TEMPLATE_TYPE % (uuid, x)
    str += ACTIVITY_TEMPLATE % (uuid, start, uuid, end, patient_id, uuid)
    return str

def map_phone_action(patient_id, phone_activity, start, end):
    uuid = generate_actid(patient_id)
    str = PHONE_FIXED % (uuid)
    for x in phone_activity.split(', '):
        str+=PHONE_TEMPLATE_TYPE % (uuid, x,uuid, x)
    str += PHONE_TEMPLATE % (uuid, start, uuid, end, patient_id, uuid)
    return str


def map_observation(metric_id,
                    source_id,
                    patient_id,
                    time_str,
                    value):

    uuid = generate_uuid(metric_id, patient_id)
    value_str, metric_group = map_value(value, metric_id)

    metric_id = metric_id.replace(' ','_')
    source_id = source_id.replace(' ','_')
    metric_id = metric_id.replace('/','_')
    source_id = source_id.replace('/','_')

    if metric_group == "CONTEXT":
        return "<http://protego.idlab.imec.be/%s/%s/obs%s>"%(patient_id, metric_id, uuid), '"%s"^^<http://www.w3.org/2001/XMLSchema#dateTime>'%(time_str), OBSERVATION_TEMPLATE_CONTEXT % (patient_id, metric_id, uuid, source_id,
                                               patient_id, metric_id, uuid, metric_id,
                                               patient_id, metric_id, uuid, time_str,
                                               patient_id, metric_id, uuid, value_str)
    elif metric_group == "WEARABLE":
        return "<http://protego.idlab.imec.be/%s/%s/obs%s>"%(patient_id, metric_id, uuid), '"%s"^^<http://www.w3.org/2001/XMLSchema#dateTime>'%(time_str), OBSERVATION_TEMPLATE_WEARABLE % (patient_id, metric_id, uuid, source_id,
                                                patient_id, metric_id, uuid, metric_id,
                                                patient_id, metric_id, uuid, time_str,
                                                patient_id, metric_id, uuid, value_str)


def map_value(value, metric_id):
    value_type, metric_group = float, None
    if metric_id in METRIC_TYPES_CONTEXT:
        value_type, metric_group = METRIC_TYPES_CONTEXT[metric_id], "CONTEXT"
    elif metric_id in METRIC_TYPES_WEARABLE:
        value_type, metric_group = METRIC_TYPES_WEARABLE[metric_id], "WEARABLE"

    if value_type == bool:
        processed_value = "true" if int(value) == 1 else "false"
    else:
        processed_value = value

    return VALUE_TEMPLATE % (processed_value, TYPE_MAP[value_type]), metric_group


# MAPPING TEMPLATES
OBSERVATION_TEMPLATE_CONTEXT = """
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/measurementMadeBy> <https://dahcc.idlab.ugent.be/Homelab/SensorsAndActuators/%s> .
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/relatesToProperty> <https://dahcc.idlab.ugent.be/Homelab/SensorsAndActuators/%s> .
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/hasTimestamp> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/hasValue> %s .
"""

OBSERVATION_TEMPLATE_WEARABLE = """
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/measurementMadeBy> <https://dahcc.idlab.ugent.be/Homelab/SensorsAndWearable/%s> .
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/relatesToProperty> <https://dahcc.idlab.ugent.be/Homelab/SensorsAndWearable/%s> .
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/hasTimestamp> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://protego.idlab.imec.be/%s/%s/obs%s> <https://saref.etsi.org/core/hasValue> %s .
"""

VALUE_TEMPLATE = "\"%s\"^^%s"

# CONVERTERS OF JSON VALUES TO ONTOLOGY CONCEPTS

METRIC_TYPES_CONTEXT = {
    "airquality.co2": int,
    "airquality.voc_total": bool,
    "energy.consumption": float,
    "energy.power": float,
    "environment.blind": float,
    "environment.button": bool,
    "environment.dimmer": float,
    "environment.light": float,
    "environment.lightswitch": bool,
    "environment.motion": bool,
    "environment.open": bool,
    "environment.relativehumidity": float,
    "environment.relay": bool,
    "environment.temperature": float,
    "environment.voltage": float,
    "environment.waterRunning::bool": bool,
    "mqtt.lastMessage": str,
    "org.dyamand.aqura.AquraLocationState_Protego User": str,
    "org.dyamand.types.airquality.CO2": float,
    "org.dyamand.types.common.AtmosphericPressure": float,
    "org.dyamand.types.common.Loudness": float,
    "org.dyamand.types.common.RelativeHumidity": float,
    "org.dyamand.types.common.Temperature": float,
    "people.presence.detected": bool,
    "people.presence.numberDetected": float,
    "weather.pressure": float,
    "weather.rainrate": float,
    "weather.windspeed": float
}

METRIC_TYPES_WEARABLE = {
    "org.dyamand.types.health.BodyTemperature": float,
    "org.dyamand.types.common.Load": float,
    "org.dyamand.types.health.DiastolicBloodPressure": float,
    "org.dyamand.types.health.HeartRate": float,
    "org.dyamand.types.health.SystolicBloodPressure": float,
    "smartphone.acceleration.x": float,
    "smartphone.acceleration.y": float,
    "smartphone.acceleration.z": float,
    "smartphone.ambient_light": float,
    "smartphone.ambient_noise.amplitude": float,
    "smartphone.ambient_noise.frequency": float,
    "smartphone.application": str,
    "smartphone.gravity.x": float,
    "smartphone.gravity.y": float,
    "smartphone.gravity.z": float,
    "smartphone.gyroscope.x": float,
    "smartphone.gyroscope.y": float,
    "smartphone.gyroscope.z": float,
    "smartphone.keyboard": str,
    "smartphone.linear_acceleration.x": float,
    "smartphone.linear_acceleration.y": float,
    "smartphone.linear_acceleration.z": float,
    "smartphone.location.accuracy": float,
    "smartphone.location.altitude": float,
    "smartphone.location.bearing": float,
    "smartphone.location.latitude": float,
    "smartphone.location.longitude": float,
    "smartphone.magnetometer.x": float,
    "smartphone.magnetometer.y": float,
    "smartphone.magnetometer.z": float,
    "smartphone.proximity": float,
    "smartphone.rotation.x": float,
    "smartphone.rotation.y": float,
    "smartphone.rotation.z": float,
    "smartphone.screen": str,
    "smartphone.sleepAPI.API_confidence": float,
    "smartphone.sleepAPI.model_type": str,
    "smartphone.sleepAPI.t_start": float,
    "smartphone.sleepAPI.t_stop": float,
    "smartphone.step": float,
    "wearable.acceleration.x": float,
    "wearable.acceleration.y": float,
    "wearable.acceleration.z": float,
    "wearable.battery_level": float,
    "wearable.bvp": float,
    "wearable.gsr": float,
    "wearable.ibi": float,
    "wearable.on_wrist": bool,
    "wearable.skt": float
}

TYPE_MAP = {
    float: "<http://www.w3.org/2001/XMLSchema#float>",
    int: "<http://www.w3.org/2001/XMLSchema#integer>",
    bool: "<http://www.w3.org/2001/XMLSchema#boolean>",
    str: "<http://www.w3.org/2001/XMLSchema#string>"
}


# HELPER FUNCTIONS

def convert_timestamp_to_string(timestamp):
    return datetime.fromtimestamp(float(timestamp) / 1000.0,
                                  pytz.timezone('Europe/Brussels')). \
        strftime('%Y-%m-%dT%H:%M:%S.%f')


def generate_uuid(metric_id, patient_id):
    key = '%s.%s' % (patient_id, metric_id)
    if key not in uuid_map:
        uuid_map[key] = 0
    result = uuid_map[key]
    uuid_map[key] += 1
    return result


def remove_whitespace(given_str):
    return ' '.join(given_str.split())
