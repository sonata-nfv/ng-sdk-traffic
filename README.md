# tng-sdk-traffic
The 5GTANGO SDK traffic generation repository

## License
The tng-sdk-traffic is published under Apache 2.0 license. Please see the LICENSE file for more details.

## CLI



## Service API
tng-sdk-traffic exposes a REST API in order to be used by any external application.

|Action|Method|Endpoint|Comment|
|------|------|--------|-------|
|Generate traffic flow.|`POST`|`/api/trafficgen/v1/flows`|Creates a traffic generation object. Traffic params are sent in a JSON configuration file.|
|Retrieve a traffic generation object|`GET`|`/api/traffgen/v1/flows/{resource_uuid}`|Gives the configuration and status of an existing traffic generation object|
|Removes traffic generation object|`DELETE`|`/api/traffgen/v1/flows/{resource_uuid}`|Removes and stops (if active) traffic generation object|
|Creates a traffic flow in existing object.|`POST`|`/api/traffgen/v1/flows/{resource_uuid}/{flow_uuid}`|Creates a specific traffic flow. Not configuration required.|
|Start/Stops an existing traffic flow in an existing object.|`PUT`|`/api/traffgen/v1/flows/{resource_uuid}/{flow_uuid}`
Modify the status the traffic flow object.|
|Retrieve status of a traffic generation flow|`GET`|`/api/traffgen/v1/flows/{resource_uuid}/{flow_uuid}`|Gives the configuration and status of an existing traffic generation object|
|Removes traffic generation flow|`DELETE`|`/api/traffgen/v1/flows/{resource_uuid}/{flow_uuid}`|It also stops the flow if it is active|

#### Lead Developers
The following lead developers are responsible for this repository and have admin rights. They can, for example, merge pull requests.

* Antón Román Portabales
* Ana Pol González

#### Feedback-Chanel
* You may use the mailing list [tango-5g-wp4@lists.atosresearch.eu](mailto:tango-5g-wp4@lists.atosresearch.eu)
* [GitHub issues](https://github.com/sonata-nfv/tng-sdk-traffic/issues)
