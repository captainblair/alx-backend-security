from django.core.management.base import BaseCommand
from ip_tracking.tasks import detect_anomalies


class Command(BaseCommand):
    help = 'Run anomaly detection manually'

    def handle(self, *args, **options):
        result = detect_anomalies()
        self.stdout.write(self.style.SUCCESS(result))