from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Contact(models.Model):

    collectionname = models.CharField("Collection Name*:", max_length=255, blank = True, null = True)
    twitterurl = models.CharField("Twitter url*:", max_length=255, blank = True, null = True,help_text="(followers < 500 ? ‘rejected’ : ‘pass’)")
    discordid = models.CharField("Discord ID*:", max_length=255, blank = True, null = True)
    email = models.EmailField("Email*:")
    stage = models.IntegerField("How will you describe your current stage of artwork*?",choices=((1, ("Stage 1: I just have started")),
                                        (2, ("Stage 2: I can generate multiple images and attributes")),
                                        (3, ("Stage 3: I have all the images and attributes for each.")),
                                        ),
                                default=1)
    description = models.TextField("Describe your project and its long term vision*:",blank=True, null=True)
    #artworkpng = models.ImageField("Send a sample of your artwork (png + json format):",upload_to = 'artwork')
    #artworkjson = models.FileField("json:",upload_to = 'artwork',validators=[FileExtensionValidator( ['json'] )])
    artworkdata = models.FileField("Send a sample of your artwork (png + json format):",upload_to = 'artwork',validators=[FileExtensionValidator( ['json','png'] )])

    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.collectionname