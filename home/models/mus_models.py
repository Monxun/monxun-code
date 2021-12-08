from django.db import models

##################################################################
#MUS

class Artist(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField()
    data = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!
    song_file = models.FileField(upload_to='songs/') # LOOKUP DJANGO DOCS 
    midi_file = models.FileField(upload_to='midi/')

    def __str__(self):
        return "%s %s" % (self.name, self.artist)