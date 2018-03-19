# tng-sdk-traffic
The 5GTANGO SDK traffic generation repository

## License
The tng-sdk-traffic is published under Apache 2.0 license. Please see the LICENSE file for more details.

## CLI

```
user@hostname:~$ tng-sdk-validate -h
usage: tng-sdk-validate [-h] [-w WORKSPACE_PATH]
                        (--project PROJECT_PATH | --package PACKAGE_FILE | --service NSD | --function VNFD)
                        [--dpath DPATH] [--dext DEXT] [--syntax] [--integrity]
                        [--topology] [--debug]
5GTANGO SDK validator
optional arguments:
  -h, --help            show this help message and exit
  -w WORKSPACE_PATH, --workspace WORKSPACE_PATH
                        Specify the directory of the SDK workspace for
                        validating the SDK project.
  --project PROJECT_PATH
                        Validate the service of the specified SDK project.
  --package PACKAGE_FILE
                        Validate the specified package descriptor.
  --service NSD         Validate the specified service descriptor. The
                        directory of descriptors referenced in the service
                        descriptor should be specified using the argument '--
                        path'.
  --function VNFD       Validate the specified function descriptor. If a
                        directory is specified, it will search for descriptor
                        files with extension defined in '--dext'
  --dpath DPATH         Specify a directory to search for descriptors.
                        Particularly useful when using the '--service'
                        argument.
  --dext DEXT           Specify the extension of descriptor files.
                        Particularly useful when using the '--function'
                        argument
  --syntax, -s          Perform a syntax validation.
  --integrity, -i       Perform an integrity validation.
  --topology, -t        Perform a network topology validation.
  --debug               Sets verbosity level to debug
Example usage:
        tng-sdk-validate --project /home/sonata/projects/project_X
                     --workspace /home/sonata/.son-workspace
        tng-sdk-validate --service ./nsd_file.yml --path ./vnfds/ --dext yml
        tng-sdk-validate --function ./vnfd_file.yml
        tng-sdk-validate --function ./vnfds/ --dext yml`
```

## Service API
tng-sdk-traffic exposes a REST API in order to be used by any external application.

#### Lead Developers
The following lead developers are responsible for this repository and have admin rights. They can, for example, merge pull requests.

* Antón Román Portabales
* Ana Pol González

#### Feedback-Chanel
* You may use the mailing list [tango-5g-wp4@lists.atosresearch.eu](mailto:tango-5g-wp4@lists.atosresearch.eu)
* [GitHub issues](https://github.com/sonata-nfv/tng-sdk-traffic/issues)
