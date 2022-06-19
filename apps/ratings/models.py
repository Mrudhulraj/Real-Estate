from django.db import models
from django.utils.translation import gettext as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampUUIDModel
from apps.profiles.models import Profile
# Create your models here.


class Rating(TimeStampUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_(
        "User providing rating"), on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(Profile, related_name="agent_rating", verbose_name=_(
        "Agent being Rated"), on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(verbose_name=_("Rating of agent"), choices=Range.choices,
                                 help_text="Poor, Fair, Good, Very Good, Excellent ", default=0)
    comment = models.TextField(verbose_name=_("Comments"))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
