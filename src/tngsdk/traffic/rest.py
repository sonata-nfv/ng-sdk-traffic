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

import os
import simplejson as json
from flask import Flask, jsonify, request
from tngsdk.traffic import traffic


app = Flask(__name__)

# Generate traffic generation object
@app.route('/api/trafficgen/v1/trafficObject', methods=['POST'])
def generate_tgo():
    body = json.loads(request.data)

    # Check existance of required data params
    if "protocol" not in body or "name" not in body:
        response = jsonify("Missing parameters to create traffic generation object")
        response.status_code = 422

        return response
    else:
        res = traffic.save_trafficObject(body)
        if (res['status'] == 200):
            response = jsonify({ "resource_uuid": res['id'] })
        else:
            response = jsonify(res['message'])
            response.status_code = res['status']
        return response


# Get list of traffic generation objects
@app.route('/api/trafficgen/v1/trafficObject', methods=['GET'])
def get_list():
    # TODO search for a traffic generation object
    return "This are the traffic generation objects"

# Get traffic generation object
@app.route('/api/trafficgen/v1/trafficObject/<int:resource_uuid>', methods=['GET'])
def get_tgo(resource_uuid):
    # TODO search for a traffic generation object
    return "This is a traffic generation object with id " + str(resource_uuid)

# Delete traffic generation object
@app.route('/api/trafficgen/v1/trafficObject/<int:resource_uuid>', methods=['DELETE'])
def delete_tgo(resource_uuid):
    # TODO delete a traffic generation object
    return "Deleting traffic generation object with id " + str(resource_uuid)

# Create traffic flow from existing traffic generation object
@app.route('/api/trafficgen/v1/flows/<int:resource_uuid>', methods=['POST'])
def generate_flow(resource_uuid):
    # TODO create a traffic flow from a traffic generation object
    return "Creating traffic flow from existing traffic generation object with id " + str(resource_uuid)

# Get traffic flow status 
@app.route('/api/trafficgen/v1/flows/<int:flow_uuid>', methods=['GET'])
def get_status(flow_uuid):
    # TODO get traffic flow status
    return "Getting traffic flow status from id " + str(flow_uuid)

# Start/Stops existing traffic flow
@app.route('/api/trafficgen/v1/flows/<int:flow_uuid>', methods=['PUT'])
def manage_flow(flow_uuid):
    # TODO start or stop a traffic flow 
    return "Starting/Stopping traffic flow with id " + str(flow_uuid)

# Removes traffic flow
@app.route('/api/trafficgen/v1/flows/<int:flow_uuid>', methods=['DELETE'])
def remove_flow(flow_uuid):
    # TODO remove a traffic flow 
    return "Deleting traffic flow with id " + str(flow_uuid)

def serve(args):
    app.run(host=args.service_address,
            port=int(args.service_port),
            debug=args.verbose)
    return