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

    elif 'detail_UUID' in args and args.detail_UUID != None:
        res = traffic.get_trafficObject(args.detail_UUID[0])['data']
        print json.dumps(res, indent=4)

    elif 'remove_UUID' in args and args.remove_UUID != None:
        res = traffic.delete_trafficObject(args.remove_UUID[0])['data']
        print json.dumps(res, indent=4)

    elif 'trafficObject' in args and args.trafficObject != None:
        jsonData = json.loads(args.trafficObject[0])
        
        if "name" in jsonData and "protocol" in jsonData \
        and jsonData['name'] != "" \
        and (jsonData['protocol'] == "UDP" or jsonData['protocol'] == "TCP"):
            res = traffic.save_trafficObject(jsonData)
            print json.dumps(res, indent=4)
            
        else: 
            print "Some of the mandatory attributes are missing or are incorrect. Please try again."

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
        nargs=1,
        required=False, 
        dest="detail_UUID" 
    )
    parser_traffic.add_argument(
        '--remove', 
        help='Remove one traffic generation object from the introduced UUID', 
        nargs=1,
        required=False, 
        dest="remove_UUID" 
    )
    parser_traffic.add_argument(
        '--add', 
        help='Create one traffic generation object of the form \'{ "name": "example", "protocol": "UDP/TCP", "description": "", "timeout": [seconds], "bandwidth": [Mbps] }\'. Only name and protocol are mandatory.', 
        nargs=1,
        required=False,
        dest="trafficObject" 
    )


    # Flows submenu 
    parser_flow = subparsers.add_parser('flow', help='Traffic flow commands')
    
    subparsers_flow = parser_flow.add_subparsers(help='Commands to operate with traffic flows')
    
    subparsers_flow.add_parser('list', help='List all the traffic flows created')
    subparsers_flow.add_parser('detail', help='List all the traffic flows created')
    subparsers_flow.add_parser('add', help='Add one traffic flow')
    subparsers_flow.add_parser('remove', help='Remove the traffic flow')

    if input_args is None:
        input_args = sys.argv[1:]
    
    return parser.parse_args(input_args)