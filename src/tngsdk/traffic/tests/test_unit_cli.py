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
# partner consortium (www.5gtango.eu

import unittest
import datetime
from tngsdk.traffic import cli, traffic


class TngSdkCliTest(unittest.TestCase):

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

    def test_cli_list(self):
        args = cli.parse_args(
            ["traffic-object", "--list"])
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 200)

    def test_cli_detail_correct(self):
        args = cli.parse_args(
            ["traffic-object", "--detail",
             "805e130b-3e54-11e8-819f-a0c5897a10ac"])
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 200)

    def test_cli_detail_incorrect(self):
        args = cli.parse_args(
            ["traffic-object", "--detail", "incorrect-id"])
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 404)

    def test_cli_remove_correct(self):
        args = cli.parse_args(
            ["traffic-object", "--remove",
             "805e130b-3e54-11e8-819f-a0c5897a10ac"])
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 200)

    def test_cli_remove_incorrect(self):
        args = cli.parse_args(
            ["traffic-object", "--remove", "incorrect-id"])
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 404)

    def test_cli_add_correct(self):
        data = {"name": "object1", "protocol": "UDP"}
        args = cli.parse_args(
            ["traffic-object", '--add',
             '{"name": "object1", "protocol": "UDP"}']
        )
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 200)

        connection = traffic.getConnection()
        cur = connection.cursor()
        cur.execute("SELECT * from trafficObjects where uuid=:id",
                    {"id": r["uuid"]})
        list = cur.fetchone()

        for i in data:
            self.assertTrue(data[i] in list)

    def test_cli_add_incorrect(self):
        args = cli.parse_args(
            ["traffic-object", "--add", '{"name": "object1"}'])
        r = cli.dispatch(args)
        self.assertEqual(r["status"], 400)


if __name__ == '__main__':
    unittest.main()
