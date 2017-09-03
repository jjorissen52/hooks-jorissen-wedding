from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Adds a schema to the database.'

    def handle(self, *args, **options):

        dbname = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        self.stdout.write(dbname)
        con = None
        con = connect(dbname=dbname, user=user, host=host, password=password)
        dbname = dbname
        self.stdout.write(self.style.SUCCESS(f'Adding schema {settings.CURRENT_SCHEMA} to database {dbname}'))
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute(f'CREATE SCHEMA {settings.CURRENT_SCHEMA};')
        cur.close()
        con.close()

        self.stdout.write(self.style.SUCCESS('All Done.'))