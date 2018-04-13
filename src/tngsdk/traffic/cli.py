# Copyright (c) 2018 5GTANGO, QUOBIS SL.
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the 5GTANGO, QUOBIS SL.
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.5gtango.eu).

import logging
import argparse
import os
import sys
import simplejson as json
from tngsdk.traffic import traffic

LOG = logging.getLogger(os.path.basename(__file__))


def dispatch(args):
    if 'list' in args and args.list:
        res = traffic.list_trafficObjects()['data']
        print json.dumps(res, indent=4)

    elif 'detail' in args and args.detail != None:
        res = traffic.get_trafficObject(args.detail[0])['data']
        print json.dumps(res, indent=4)

    elif 'remove' in args and args.remove != None:
        res = traffic.delete_trafficObject(args.remove[0])['data']
        print json.dumps(res, indent=4)

    elif 'add' in args and args.add != None:
        jsonData = json.loads(args.add[0])
        
        if "name" in jsonData and "protocol" in jsonData \
        and jsonData['name'] != "" \
        and (jsonData['protocol'] == "UDP" or jsonData['protocol'] == "TCP"):
            res = traffic.save_trafficObject(jsonData)
            print json.dumps(res, indent=4)
            
        else: 
            print "JSON data is missing or incorrect. Please try again."
    
    elif 'flow_status' in args and args.flow_status and args.flow_uuid:
        print "This will check flow status"
    
    elif 'flow_add' in args and args.flow_add:
        print "This will add a flow"

    elif 'flow_remove' in args and args.flow_remove and args.flow_uuid:
        print "This will remove a flow"

    elif ('flow_start' in args and args.flow_start) or \
        ('flow_stop' in args and args.flow_stop) and args.flow_uuid:
        print "This will start or stop a flow"
    
    return  


def parse_args(input_args=None):
    parser = argparse.ArgumentParser(
        prog="tng-sdk-traffic",
        description="5GTANGO SDK traffic generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Example usage:
        tng-sdk-traffic service --address 127.0.0.1 --port 8000
        """)
    
    parser.add_argument(
        "--verbose",
        help="Sets verbosity level to debug",
        dest="verbose",
        action="store_true",
        required=False,
        default=False
    )

    subparsers = parser.add_subparsers(help='Commands offered by the traffic generation tool')

    # Launch as REST API
    parser_service = subparsers.add_parser(
        'service', 
        help='Launch tng-sdk-traffic in service mode'
    )
    parser_service.add_argument(
        "--address",
        help="Listen address of REST API when in service mode."
        + "\nDefault: 127.0.0.1",
        required=False,
        default="127.0.0.1",
        dest="service_address"
    )
    parser_service.add_argument(
        "--port",
        help="TCP port of REST API when in service mode."
        + "\nDefault: 8090",
        required=False,
        default=8090,
        dest="service_port"
    )


    # Traffic generation object submenu 
    parser_traffic = subparsers.add_parser('traffic-object', help='Traffic generation object commands')

    parser_traffic.add_argument(
        '--list', 
        help='List all the traffic generation objects', 
        required=False, 
        action="store_true",
        dest="list"
    )
    parser_traffic.add_argument(
        '--detail', 
        help='Show one traffic generation object details from the introduced UUID', 
        required=False,
        nargs=1,
        metavar=('UUID'),
        dest="detail"
    )
    parser_traffic.add_argument(
        '--remove', 
        help='Remove one traffic generation object from the introduced UUID', 
        required=False,
        nargs=1,
        metavar=('UUID'),
        dest="remove"
    )
    parser_traffic.add_argument(
        '--add', 
        help='Create one traffic generation object of the form \'{ "name": "example", \
        "protocol": "UDP/TCP", "description": "", "timeout": [seconds], \
        "bandwidth": [Mbps] }\'. Only name and protocol are mandatory.', 
        required=False,
        nargs=1,
        metavar=('TRAFFIC OBJECT'),
        dest="add" 
    )


    # Flows submenu 
    parser_flow = subparsers.add_parser('flow', help='Traffic flow commands')
    
    parser_flow.add_argument(
        '--flow-add', 
        help='Creates a traffic flow from one traffic generation object UUID', 
        required=False,
        action="store_true", 
    )
    parser_flow.add_argument(
        '--flow-start', 
        help='Starts a traffic flow from its UUID', 
        required=False,
        action="store_true", 
    )
    parser_flow.add_argument(
        '--flow-stop', 
        help='Stops a traffic flow from its UUID', 
        required=False,
        action="store_true", 
    )
    parser_flow.add_argument(
        '--flow-status', 
        help='Retrieves the status of a traffic flow from its UUID', 
        required=False, 
        action="store_true"
    )
    parser_flow.add_argument(
        '--flow-remove', 
        help='Remove one traffic flow from its UUID', 
        required=False,
        action="store_true", 
    )
    parser_flow.add_argument(
        '--flow-uuid', 
        help='UUID of the desired traffic flow', 
        nargs=1,
        required=False
    )

    if input_args is None:
        input_args = sys.argv[1:]

    # Check at least one of the main commands were introduced
    if "-h" not in input_args and "service" not in input_args and \
        "traffic-object" not in input_args and "flow" not in input_args:
        if "-h" not in input_args:
            print "Please, select one of the offered commands to continue.\n"
            parser.print_help()
            sys.exit(0)

    # Check at least one traffic-object command were introduced
    elif "traffic-object" in input_args and len(input_args) == 1:
        print "Please choose a command from the list below.\n"
        parser_traffic.print_help()

    # Check at least one traffic-object command were introduced
    elif "flow" in input_args and len(input_args) == 1:
        print "Please choose a command from the list below.\n"
        parser_flow.print_help()

    return parser.parse_args(input_args)