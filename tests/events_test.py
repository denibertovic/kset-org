from django.test import TestCase

from .base import BaseTestClient


__all__ = ['EventsViewTest']


class EventsViewTest(TestCase):

    def setUp(self):
        super(EventsViewTest, self).setUp()
        self.client = BaseTestClient()

    def test_get_events_archive(self):
        # self.client.login(username='super_user',
        #     password='foobar')

        response = self.client.get('events-archive')
        print response
        self.assertEquals(200, response.status_code)