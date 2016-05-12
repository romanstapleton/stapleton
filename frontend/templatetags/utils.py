from django import template
register = template.Library()


@register.filter
def name_format(value):
    name_map = {
        'itunes': "iTunes",
        'amazon': "Amazon",
        'spotify': "Spotify",
        'sound_cloud': "Sound Cloud",
        'apple_music': "Apple Music",
        'google_play': 'Google Play',
        'rdio': "Rdio",
        'deezer': "Deezer",
        'tidal': "Tidal",
        'youtube': "YouTube",
        'microsoft_groove': "Microsoft Groove",
        'medianet': "MediaNet",
        'shazam': "Shazam",
    }
    if value in name_map:
        value = name_map.get(value)
    return value
