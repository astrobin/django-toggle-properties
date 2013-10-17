import unittest

from django.db import models
from django.contrib.auth.models import User

from models import ToggleProperty

class BaseFavoriteTestCase(unittest.TestCase):
    def setUp(self):
        self.users = dict([(u.username, u) for u in User.objects.all()])
        if len(self.users) != 4:
            for name in ['alice', 'bob', 'chris', 'dawn']:
                try:
                    u = User.objects.create(username=name)
                    self.users[name] = u
                except:
                    pass

class TogglePropertyTestCase(BaseFavoriteTestCase):
    def testAddToggleProperty(self):
        """ Add alice as a Like of chris, add the Like as a Like
        of alice
        """
        chris = self.users['chris']
        alice = self.users['alice']
        like = ToggleProperty.objects.create_toggleproperty("like", chris, alice)

        self.assertEquals(like.user, chris)
        self.assertEquals(like.content_object, alice)

        meta_like = ToggleProperty.objects.create_toggleproperty("like", alice, like)

        self.assertEquals(meta_like.user, alice)
        self.assertEquals(meta_like.content_object, like)

    def testGetTogglePropertiesForUser(self):
        """ Get likes for chris """
        chris = self.users['chris']
        alice = self.users['alice']

        # verify that people can get them
        likes = ToggleProperty.objects.toggleproperties_for_user("like", chris)

        self.assertEquals(len(likes), 1)
        self.assertEquals(likes[0].content_object, self.users['alice'])

    def testGetTogglePropertiesForModel(self):
        alice = self.users['alice']

        # the meta like
        meta_like = ToggleProperty.objects.get(pk=2)

        likes = ToggleProperty.objects.toggleproperties_for_model("like", ToggleProperty)

        self.assertEquals(len(likes), 1)
        self.assertEquals(likes[0], meta_likes)
        self.assertEquals(likes[0].user, alice)

    def testGetTogglePropertiesForObject(self):
        alice = self.users['alice']

        like = ToggleProperty.objects.get(pk=1)

        likes = ToggleProperty.objects.toggleproperties_for_object("like", like)
        self.assertEquals(len(likes), 1)
        self.assertEquals(likes[0].user, alice)

