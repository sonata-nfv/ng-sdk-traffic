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

import unittest
import datetime
from tngsdk.traffic import traffic


class TngSdkTrafficTest(unittest.TestCase):

    def setUp(self):
        traffic.start_dbconnection("trafficTesting.db")
        connection = traffic.getConnection()
        cur = connection.cursor()
        cur.execute("insert into trafficObjects VALUES('805e130b-3e54-11e8-819f-a0c5897a10ac', \
                    'object 1', '%s', 'UDP', 'Description 1', '10000', '1');" %
                    (str(datetime.datetime.now())))
        cur.execute("insert into trafficObjects VALUES('805edf12-3e54-11e8-819f-b0c5265a10bc', \
                    'object 2', '%s', 'TCP', 'Description 2', '2000', '2');" %
                    (str(datetime.datetime.now())))
        cur.execute("insert into trafficObjects VALUES('805ff323-3e54-11e8-819f-d0c354a101ah', \
                    'object 3', '%s', 'UDP', 'Description 3', '5000', '1');" %
                    (str(datetime.datetime.now())))
        connection.commit()

    def tearDown(self):
        connection = traffic.getConnection()
        cur = connection.cursor()
        cur.execute("DROP TABLE trafficObjects")

    def test_traffic_add_correct(self):
        data = {"name": "Test Object", "protocol": "TCP"}
        state = traffic.save_trafficObject(data)
        self.assertEqual(state['status'], 200)

        connection = traffic.getConnection()
        cur = connection.cursor()
        cur.execute("SELECT * from trafficObjects where uuid=:id",
                    {"id": state["uuid"]})
        list = cur.fetchone()

        for i in data:
            self.assertTrue(data[i] in list)

    def test_traffic_add_incorrect(self):
        data = {"name": "name1"}
        state = traffic.save_trafficObject(data)
        self.assertEqual(state['status'], 400)

    def test_traffic_list(self):
        state = traffic.list_trafficObjects()
        self.assertEqual(state["status"], 200)

    def test_traffic_delete_correct(self):
        data = traffic.list_trafficObjects()
        state = traffic.delete_trafficObject(data['data'][1]["uuid"])
        self.assertEqual(state["status"], 200)

    def test_traffic_delete_incorrect(self):
        state = traffic.delete_trafficObject("incorrectID")
        self.assertEqual(state["status"], 404)

    def test_traffic_detail_correct(self):
        state = traffic.get_trafficObject('805e130b-3e54-11e8-819f-a0c5897a10ac')
        self.assertEqual(state['status'], 200)

    def test_traffic_detail_incorrect(self):
        state = traffic.get_trafficObject("incorrectID")
        self.assertEqual(state['status'], 404)


if __name__ == '__main__':
    unittest.main()
