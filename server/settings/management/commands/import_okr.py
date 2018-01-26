import csv
import re
from datetime import datetime

import requests
import zeep
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from player.models import Player
from rating.models import Rating, RatingResult
from settings.models import Country, City
from tournament.models import Tournament, TournamentResult


def get_date_string():
    return timezone.now().strftime('%H:%M:%S')


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('{0}: Start'.format(get_date_string()))

        rating = Rating.objects.get(type=Rating.OKR)
        rating.updated_on = timezone.now()
        rating.save()

        RatingResult.objects.filter(rating=rating).delete()

        wsdl = 'http://niichi.lorien.biz/cxf/niichi/portal?wsdl'
        client = zeep.Client(wsdl=wsdl)
        results = client.service.getStatistics()
        for result in results:
            temp = result['name'].split(' ')
            last_name = temp[0]
            first_name = temp[1]

            player = None

            try:
                player = Player.objects.get(first_name_ru=first_name, last_name_ru=last_name)
            except Player.DoesNotExist:
                try:
                    replaced_first_name = first_name.replace('е', 'ё')
                    replaced_last_name = last_name.replace('е', 'ё')
                    player = Player.objects.get(first_name_ru=replaced_first_name, last_name_ru=replaced_last_name)
                except Player.DoesNotExist:
                    pass

            # if not player:
            #     print('Not found player', last_name, first_name)

            if player:
                player.okr_id = result['id']
                player.save()

                RatingResult.objects.create(
                    rating=rating,
                    player=player,
                    score=result['rate'],
                    average_place=result['averagePlace'],
                    first_place=result['place1Percent'],
                    second_place=result['place2Percent'],
                    third_place=result['place3Percent'],
                    fourth_place=result['place4Percent'],
                    tenhou_rank=result['tenhouRank'],
                    games_count=result['gameCount'],
                )

        results = RatingResult.objects.filter(rating=rating).order_by('-score')

        place = 1
        for result in results:
            result.place = place
            result.save()

            place += 1

        print('{0}: End'.format(get_date_string()))
