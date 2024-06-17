from django.db import models
import json


class Bookmaker(models.Model):
    name = models.CharField(max_length=255)
    nomenclature = models.JSONField()
    base_url = models.URLField()
    url_for_sport = models.URLField()
    url_for_match_detail = models.URLField()
    sports = models.ManyToManyField('Sport', related_name='bookmakers')
    matches = models.ManyToManyField('Match', related_name='bookmakers')

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=255)
    matches = models.ManyToManyField('Match', related_name='sports')

    def __str__(self):
        return self.name


class Match(models.Model):
    matchid = models.CharField(max_length=255)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    markets = models.ManyToManyField('Market', related_name='matches')

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


class Market(models.Model):
    name = models.CharField(max_length=255)
    odds = models.TextField()  # Store odds as a JSON string

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.name


class Arbitrage(models.Model):
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name='arbitrages')
    market = models.ForeignKey(
        Market, on_delete=models.CASCADE, related_name='arbitrages')
    bookmakers = models.ManyToManyField(Bookmaker, related_name='arbitrages')
    odds = odds = models.TextField()  # Store odds as a JSON string
    profit = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return f"Arbitrage Opportunity in {self.match} - Market: {self.market}"
