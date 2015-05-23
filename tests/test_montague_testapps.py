from __future__ import absolute_import

from montague_testapps.apps import basic_app, make_basic_app


def test_app_factories():
    assert make_basic_app({}) is basic_app
