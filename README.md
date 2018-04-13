# tng-sdk-traffic

The 5GTANGO SDK traffic generation repository is part of the European H2020 project 5GTANGO NFV SDK. This component can be used to generate customized traffic to an specific IP and port. tng-sdk-traffic can be used through the CLI or as a micro-service running inside a docker container.

## Installation

```
python setup.py install
```

### Dependencies

* SQLite3

## Usage

### CLI mode

The CLI interface is designed for developer usage, allowing to quickly generate traffic for 5GTANGO project. The possibilities offered by this tool are displayed below:

* service is used to launch the API REST
* traffic-object is used to operate with the traffic generation objects. It allows creation, listing, detailed view and removal
* flow is used to operate with the traffic flows. It allows creation, status retrieval, removal and start/stop the traffic flows

```
> tng-sdk-traffic
Please, select one of the offered commands to continue.

usage: tng-sdk-traffic [-h] [--verbose] {service,traffic-object,flow} ...

5GTANGO SDK traffic generator

positional arguments:
  {service,traffic-object,flow}
                        Commands offered by the traffic generation tool
    service             Launch tng-sdk-traffic in service mode
    traffic-object      Traffic generation object commands
    flow                Traffic flow commands

optional arguments:
  -h, --help            show this help message and exit
  --verbose             Sets verbosity level to debug

Example usage:
        tng-sdk-traffic service --address 127.0.0.1 --port 8000

        tng-sdk-traffic traffic-object --list
        tng-sdk-traffic traffic-object --add '{"name": "object1", "protocol": "UDP"}'
        tng-sdk-traffic traffic-object --detail 805e130b-3e54-11e8-819f-a0c5897a10ac
        tng-sdk-traffic traffic-object --remove 805e130b-3e54-11e8-819f-a0c5897a10ac

        tng-sdk-traffic flow --start 805e130b-3e54-11e8-819f-a0c5897a10ac
```

### Service mode

tng-sdk-traffic exposes a REST API in order to be used by any external application.

Initial path for the end-points in the current version: `/api/trafficgen/v1`

| Action                                                     | Method   | Endpoint                         | Comment                                                                                    |
| ---------------------------------------------------------- | -------- | -------------------------------- | ------------------------------------------------------------------------------------------ |
| Generate traffic generation object                         | `POST`   | `/trafficObject`                 | Creates a traffic generation object. Traffic params are sent in a JSON configuration file. |
| Retrieve a list of traffic generation objects              | `GET`    | `/trafficObject`                 | Gives a list of the created traffic generation objects.                                    |
| Retrieve a traffic generation object                       | `GET`    | `/trafficObject/{resource_uuid}` | Gives the configuration and status of an existing traffic generation object.               |
| Removes traffic generation object                          | `DELETE` | `/trafficObject/{resource_uuid}` | Removes and stops (if active) traffic generation object.                                   |
| Creates a traffic flow in existing object                  | `POST`   | `/flows/{flow_uuid}`             | Creates a specific traffic flow. Not configuration required.                               |
| Start/Stops an existing traffic flow in an existing object | `PUT`    | `/flows/{flow_uuid}`             | Modify the status the traffic flow object.                                                 |
| Retrieve status of a traffic generation flow               | `GET`    | `/flows/{flow_uuid}`             | Gives the configuration and status of an existing traffic generation object.               |
| Removes traffic generation flow                            | `DELETE` | `/flows/{flow_uuid}`             | It also stops the flow if it is active.                                                    |

### Examples of use

1.  Launch as a service against localhost:

    `tng-sdk-traffic --service --address 127.0.0.1 --port 8000`

2.  List the traffic objects created:

    `tng-sdk-traffic traffic-object --list`

3.  Add a traffic object to the DB:

    `tng-sdk-traffic traffic-object --add '{"name": "object1", "protocol": "UDP"}'`

4.  View details of a traffic object:

    `tng-sdk-traffic traffic-object --detail 805e130b-3e54-11e8-819f-a0c5897a10ac`

5.  Remove a traffic object:

    `tng-sdk-traffic traffic-object --remove 805e130b-3e54-11e8-819f-a0c5897a10ac`

6.  Start a traffic flow:

    `tng-sdk-traffic flow --start 805e130b-3e54-11e8-819f-a0c5897a10ac`

## Documentation

TODO (e.g. link to wiki page)

## Development

To contribute to the development of this 5GTANGO component, you may use the very same development workflow as for any other 5GTANGO Github project. That is, you have to fork the repository and create pull requests.

## License

The tng-sdk-traffic is published under Apache 2.0 license. Please see the LICENSE file for more details.

#### Lead Developers

The following lead developers are responsible for this repository and have admin rights. They can, for example, merge pull requests.

* Antón Román Portabales
* Ana Pol González

#### Feedback-Chanel

* You may use the mailing list [tango-5g-wp4@lists.atosresearch.eu](mailto:tango-5g-wp4@lists.atosresearch.eu)
* [GitHub issues](https://github.com/sonata-nfv/tng-sdk-traffic/issues)
