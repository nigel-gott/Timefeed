"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from timefeed.apps.feed.models import Feed

class FeedTest(TestCase):
    def test_feed_model_name(self):
        test_name = "TEST2"

        feed = Feed(name=test_name)
        self.assertEquals(feed.name, test_name)
