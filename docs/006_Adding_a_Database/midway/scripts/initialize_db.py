import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    peter = models.horse.Horse(name='Peter')
    dbsession.add(peter)

    lois = models.horse.Horse(name='Lois')
    dbsession.add(lois)

    meg = models.horse.Horse(name='Meg')
    dbsession.add(meg)

    chris = models.horse.Horse(name='Chris')
    dbsession.add(chris)

    Stewie = models.horse.Horse(name='Stewie')
    dbsession.add(Stewie)

    Rupert = models.horse.Horse(name='Rupert')
    dbsession.add(Rupert)

    Brian = models.horse.Horse(name='Brian')
    dbsession.add(Brian)

    Cleveland = models.horse.Horse(name='Cleveland')
    dbsession.add(Cleveland)

    joe = models.horse.Horse(name='Joe')
    dbsession.add(joe)

    Quagmire = models.horse.Horse(name='Quagmire')
    dbsession.add(Quagmire)

    race = models.race.Race(race_number=0, score=100, horse_id=1)
    dbsession.add(race)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
