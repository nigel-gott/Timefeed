"""
Data models used to represent Feeds and their Events.
""" 

from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    """
        A Feed is a named and owned collection of Events. Other users can
        subscribe to a given Feed. A Feed must have an owner and a name.
    """
    name = models.CharField(max_length = 30, blank=False)
    description = models.TextField(blank=True)

    owner = models.ForeignKey(
            User, 
            related_name='owned_feeds', 
            null=False,
            blank=False
            )

    subscribers = models.ManyToManyField(
            User, 
            null=True, 
            blank=True, 
            related_name='subscribed_feeds'
            )

    def __unicode__(self):
        return "Feed: " + self.name + " owned by "

    class Meta:
        unique_together = ('name', 'owner',)

class Event(models.Model):
    """
        An Event always associated with a single Feed. The owner of the Feed is
        also the owner of the event. 
    """

    name = models.CharField(max_length = 30, blank=False)
    description = models.TextField(blank=True)

    start = models.DateTimeField(blank=False, null=False)
    end = models.DateTimeField(blank=False, null=False)

    timefeed = models.ForeignKey(Feed, blank=False, null=False)

