import datadog
import logging
import os
import time

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

host = os.getenv('DD_AGENT_HOST')
if not host:
    log.error('DD_AGENT_HOST is not set! Cannot continue.')
    exit(1)

port = os.getenv('DD_DOGSTATSD_PORT')
if not port:
    log.error('DD_DOGSTATSD_PORT is not set! Cannot continue.')
    exit(1)

host_alnum = ''.join(filter(str.isalnum, host))
metric = f'datadog_sender.test_metric.works.{host_alnum}'

log.info(f'Sending metrics to {host}:{port}')

datadog.initialize()
log.info('Datadog initialized')

while True:
    datadog.statsd.increment(metric)
    log.info(f'Incremented {metric}')
    time.sleep(5)
