from django.db import models

class EEGFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='eeg_files/')
    recording_date = models.DateTimeField(null=True, blank=True)
    num_signals = models.IntegerField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    sampling_rates = models.JSONField(default=dict)
    channel_names = models.JSONField(default=list)

    def __str__(self):
        return f"EEG File {self.id}"