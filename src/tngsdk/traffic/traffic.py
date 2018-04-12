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
import sys
import logging
import datetime
import sqlite3 as lite


LOG = logging.getLogger(os.path.basename(__file__))

connection = None

def start_dbconnection():
    try:
        global connection
        connection = lite.connect('traffic.db')
        create_dbtables()

    except lite.Error, e:
        LOG.error("Error %s:" % e.args[0])
        sys.exit(1)

def create_dbtables():
    try:
        cur = connection.cursor()           
        cur.execute('CREATE TABLE IF NOT EXISTS trafficObjects( \
                    name text NOT NULL, \
                    creation_date text NOT NULL, \
                    protocol text NOT NULL, \
                    description text, \
                    timeout text, \
                    bandwidth text);')

    except lite.Error, e:
        LOG.error("Error %s:" % e.args[0])
        sys.exit(1)

def save_trafficObject(data):
    creation_date = str(datetime.datetime.now())

    # Required parameters
    name = data['name']
    protocol = data['protocol']

    # Optional parameters
    if "timeout" in data:
        timeout = data['timeout']
    else:
        timeout = None
    if "bandwidth" in data:
        bandwidth = data['bandwidth']
    else:
        bandwidth = None
    if "description" in data:
        description = data['description']
    else:
        description = None
            
    try:
        cur = connection.cursor()           
        cur.execute("insert into trafficObjects VALUES('%s', '%s', '%s', '%s', '%s', '%s');" % \
                    (name, creation_date, protocol, description, timeout, bandwidth))
        connection.commit()

        return { "status": 200, "id": cur.lastrowid }

    except lite.Error, e:
        LOG.error("Error %s:" % e.args[0])
        return { "status": 422, "message": "Unable to store the traffic generation object" }
