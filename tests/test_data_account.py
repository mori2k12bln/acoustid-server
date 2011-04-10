# Copyright (C) 2011 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details. 

from nose.tools import *
from tests import prepare_database, with_database
from acoustid.data.account import lookup_account_id_by_apikey


@with_database
def test_lookup_account_id_by_apikey(conn):
    prepare_database(conn, """
INSERT INTO account (name, apikey) VALUES ('User', 'userkey');
""")
    id = lookup_account_id_by_apikey(conn, 'userkey')
    assert_equals(1, id)
    id = lookup_account_id_by_apikey(conn, 'foooo')
    assert_equals(None, id)
