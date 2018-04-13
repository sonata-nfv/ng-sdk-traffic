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

1.  Launch as a service against localhost: `tng-sdk-traffic --service --address 127.0.0.1 --port 8000`

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
