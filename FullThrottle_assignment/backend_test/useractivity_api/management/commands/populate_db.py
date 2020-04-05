from django.core.management.base import BaseCommand
from useractivity_api.models import User
from useractivity_api.models import ActivityPeriods
from django.utils.crypto import get_random_string
# import random
from random import randrange
from datetime import datetime, timedelta
import string
from faker import Faker  # faker is used to create dummy data for testing purpose

fake = Faker()  # creates a object for faker class


class Command(BaseCommand):
    help = 'populate data into database'

    def generate_id(self):
        # generates a random id for user
        id = get_random_string(9, string.ascii_uppercase + string.digits)
        return id

    def gen_datetime(self, start, end):
        # generate a datetime  between two given dates
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        st_date = start + timedelta(seconds=random_second)
        en_date = st_date + timedelta(seconds=delta.seconds)
        list1 = [st_date, en_date]
        return list1

    def add_arguments(self, parser):
        # this funtion will take the no of user to be created from the terminal
        parser.add_argument('no_of_user', type=int)

    def handle(self, *args, **kwargs):
        # this function will create the dummy user and related data and store it to database
        no_user = kwargs['no_of_user']
        for i in range(no_user):
            e_id = self.generate_id()
            user = User(id=e_id, real_name=fake.name(), tz=fake.timezone())
            user.save()
            # random_no = random.randrange(1,4); use this syntax to randomly generate no of active sessions
            for x in range(3):
                start_time = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
                end_time = datetime.strptime('2/3/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
                time_list = self.gen_datetime(start_time, end_time)
                str_time = datetime.strftime(time_list[0], "%b %d %Y %I:%M%p")
                e_time = datetime.strftime(time_list[1], "%b %d %Y %I:%M%p")
                activity_period = ActivityPeriods(user_id=user, start_time=str_time, end_time=e_time)
                activity_period.save()
        print("No of user created :", no_user)
