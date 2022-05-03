### Guide to run the semantic rule mining applications

A rule mining application was built on protego dataset and corresponding knwoledge (see [dataset](https://dahcc.idlab.ugent.be/dataset.html)).
Here, we try to mine a general rule for one or more performed life style activities performed and annotated by the protego participants.
This section describes how you can run this application and what will be the expected outcome.

To make sure you can run this application, the following software must be installed:
- [Stardog](https://www.stardog.com) is being used as a triple store inside this application, make sure you run a local copy of it before executing the python scripts
- [INK](https://github.com/IBCNServices/INK) is used to transform the generated knowledge graph into an interpretable embedding (which is later on being used to mine rules)
- [Skope-rules](https://github.com/scikit-learn-contrib/skope-rules) is being used to mine the corresponding rules.

To run this applications:
1) ExtendedObservations.py - Generate the KG files based on the raw sensor data (or you can directly use the seperated KG files on https://dahcc.idlab.ugent.be/dataset.html)
and generate new, more advanced observations from them using the rules within rule.ttl. These new observations, together with the transformed activities and full protego DAHCC ontology
are loaded within the Stardog.
2) rulemining.py - Create the INK representation for all life style activities within the Stardog database. Split the generated embeddings in a positive and negative set, based on the activity were you want to learn a rule for. Mine rules and return the result.

An example of such a mined rule could look like this:

<table>
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Event</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Rule</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Precision</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Recall</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Shower</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">'hasEvent.kitchen.Temperature &gt; 21.75 </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">and hasEvent.toilet2.Loudness_mean &gt; 46.83  </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">and </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">NOT hasEvent.using§kitchen</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.9411</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.6153</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Toilet</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">hasEvent.LightSwitchOnIn§toilet1 and NOT hasEvent.personIn§kitchen and hasEvent.using§homelab</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.8175</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.5734</span></td>
  </tr>
</tbody>
</table>
