

# What is DAHCC?
Data Analytics in Healthcare and Connected Care (DAHCC for short) combines knowledge and data to describe person activities, the context/profile of the involved users, daily care operations, emergency call handling processes. 

*DAHCC provides both data and metadata to describe multiple data analytics components, interlink them, and show their application potential*

# Why DAHCC?

Ambient intelligence, where numerous IoT devices work together to support caregivers and residents in carrying out their everyday activities and tasks, are needed to keep more residents at home.

To reduce the workload for the caregivers, the data available from these devices must be linked, combined, aggregated and provided in a machine readable format such that intelligent systems can reason or derive information to assist in the daily care process of people.

The available exisitng systems and resources only describes one facet (they can describe IoT devices in a home setting, without describing the data analytics performed on the gathered data).

DAHCC changes this, by providing both datasets with daily life activities and a complementary, reusable ontology which combine IoT components with healthcare and data analytical concepts.

## DAHCC ontology

Ontology capturing all background & domain knowledge required about call handling processes & context/profile of the involved users to feed contextual AI services. The DAHCC ontology imports well-known concepts from other, established industry standards:

 * [SAREF core](https://saref.etsi.org/core/v3.1.1/), to link sensors and sensor proerties,
* [SAREF4BLDG](https://saref.etsi.org/saref4bldg/v1.1.2/), to link sensors & devices with their physical location,
* [SAREF4WEAR](https://saref.etsi.org/saref4wear/v1.1.1/), to link wearables and wearable properties
* [SAREF4EHAW](https://saref.etsi.org/saref4ehaw/)) standard, to link medical data and sensors to patients and caretakers, 
* [The Executor, Execution, Procedure (EEP) ontology](https://iesnaola.github.io/EEP/index-en.html) to show the interaction between the Machine Learning (ML) concepts.
* [The GeoSPARQL ontology](https://opengeospatial.github.io/ogc-geosparql/geosparql11/index.html)
* [OWL time ontology](https://www.w3.org/TR/owl-time/)
* [The SSN ontology](https://www.w3.org/TR/vocab-ssn/) (compatability use cases).


The design of this ontology was based on three types of information sources:

1.  A lot of information and background knowledge was already readily available in structured documents, e.g. the descriptions of used sensors and monitoring systems in technical specifications & APIs
2.  An assessment was also performed of existing ontologies that could be reused.
3.  Some knowledge was only available from industry partners, who perform day-to-day call assessment & handling based on experience. To derive this information, decision tree workshops were organized with nurses and call operators.

In the end, the DAHCC ontology existed of 5 interacting sub ontologies, each describing a subpart of the connected care process.  Full detailed ontology documentation are available in the [Ontologies](https://dahcc.idlab.ugent.be/ActivityRecognition.html) section

<img width="1242" alt="DHACC_overview" src="https://dahcc.idlab.ugent.be/dahcc_overview.png">

## DAHCC datasets

Data captured in a daily life setting, gathered through IoT sensors in households and wearables attached to residents were semantically enriched through the DAHCC ontology. More information about these datasets can be found in the [Ontologies](https://dahcc.idlab.ugent.be/Datasets.html) section. 


## DAHCC Applications

Numerous applications can be build based on the available DAHCC resources. More information about these applications can be found in the [Applications](https://dahcc.idlab.ugent.be/Applications.html) section. 

# Referencing
If you use the DAHCC in a scholarly article, we would appreciate a citation:

```
@misc{dahccontology,
  author       = {Bram Steenwinckel and Mathias De Brouwer and Femke Ongenae},
  title        = {{DAHCC: The Data Analytics in Healthcare and Connected Care ontology}},
  organization = {IDLab},
  year         = {2022},
  url          = {https://dahcc.idlab.ugent.be}
}
```


