### Guide to run the semantic rule mining applications

A higher-order semantic event creation application was designed to transform the raw data samples within the DAHCC protego dataset into more advanced semantic events.
A combination of mapping the raw observations to semantic data and a reasoning engine was used to define those higer-order events.

To make sure you can run this application, the following software must be installed:
- [Stardog](https://www.stardog.com) is being used as a triple store inside this application, make sure you run a local copy of it before executing the python scripts. Stardog's internal reasoning capabilities are also used to derive the more advanced events.

To run this applications:
1) ExtendedObservations.py - Generate the KG files based on the raw sensor data (or you can directly use the seperated KG files on https://dahcc.idlab.ugent.be/dataset.html)
and generate new, more advanced events from them using the rules within rule.ttl. These new events, together with the transformed activities and full protego DAHCC ontology
are loaded within a new Stardog database and can be analysed further on.
