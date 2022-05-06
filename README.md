

# What is DAHCC?
Data Analytics in Health and Connected Care (DAHCC) resembles both the way and the data to describe the connected care applications, the used sensors to create such care applications together with their link to the people who are involved by or with those care applications (e.g. patients, healthcare professionals etc.).

The DAHCC resource exists out of 3 main components:

[A large dataset of daily life activities](https://dahcc.idlab.ugent.be/dataset.html), bot provided in raw and knowledge graph format.<br>
[The DAHCC Ontology](https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/) capturing care, patient, daily life activity recognition and lifestyle domain knowledge.<br>
[Connected Care Applications](https://dahcc.idlab.ugent.be/Applications.html) which shows the potential of combining data with ontological meta-data.<br>

# Why DAHCC?

To achieve a pervasive healthcare follow-up of (chronic) diseases, connected care applications have become increasingly used. Within these applications, objective insights about the patients are collected by using AI models on IoT devices in their homes and wearable devices to capture biomedical parameters. 

However, to enable easy re-use of AI algorithms and applications trained and designed on top of this sensor data, it is important to uniformly describe the collected data and how this links to the health condition of the patient. 

The DAHCC ontology allows capturing the metadata about the sensors and data, the different designed AI algorithms and the health insights they derive and how this is correlated to the medical condition of the patients. By providing this uniform metadata, applications can be more easily integrated into large care systems.

# Referencing
The ontology, the datasets, the KG and the applications are all made open-source under an [MIT license](https://github.com/predict-idlab/DAHCC-Sources/blob/main/LICENSE).

If you use DAHCC in a scholarly article, we would appreciate a citation:

```
@misc{dahcc_resource,
  author    = {{Bram Steenwinckel, Mathias De Brouwer, Marija Stojchevska, Jeroen Van Der Donckt, Jelle Nelis, Joeri Ruyssinck, Joachim 
                  van der Herten, Koen Casier, Jan Van Ooteghem, Pieter Crombez, Filip De Turck, Sofie Van Hoecke and Femke Ongenae}},
  title     = {{Data Analytics For Health and Connected Care: Ontology, Knowledge Graph and Applications}},
  year      = {2022},
  url       = {https://dahcc.idlab.ugent.be}
}
```
