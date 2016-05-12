from __future__ import unicode_literals
from django.db import models
from cloudinary.models import CloudinaryField


RELEASE_TYPE_CHOICES = (
    ('A', 'Album'),
    ('S', 'Single'),
)


class Release(models.Model):
    title = models.CharField(max_length=30, blank=False, null=True)
    type = models.CharField('Album or single?', choices=RELEASE_TYPE_CHOICES, null=True, blank=True, max_length=1)
    date = models.DateTimeField(blank=False, null=True)
    cover = CloudinaryField('Cover image', null=True, blank=True)
    itunes = models.URLField(blank=True, null=True)
    apple_music = models.URLField(blank=True, null=True)
    google_play = models.URLField(blank=True, null=True)
    spotify = models.URLField(blank=True, null=True)
    sound_cloud = models.URLField(blank=True, null=True)
    amazon = models.URLField(blank=True, null=True)
    rdio = models.URLField(blank=True, null=True)
    deezer = models.URLField(blank=True, null=True)
    tidal = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    microsoft_groove = models.URLField(blank=True, null=True)
    medianet = models.URLField(blank=True, null=True)
    shazam = models.URLField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.title

    def get_cover(self):
        """Returns URL for album/single cover, loaded to the image storage"""
        return self.cover.build_url(width=436, height=436, crop='fit') if self.cover else ""
