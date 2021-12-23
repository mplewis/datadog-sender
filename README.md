# datadog-sender

Quick and dirty container to send metrics to a target [DogStatsD](https://docs.datadoghq.com/metrics/dogstatsd_metrics_submission/) forwarder using the [Datadog Python](https://pypi.org/project/datadog/) library.

# Usage

The following env vars must be set:

| Variable            | Description                        | Example     |
| ------------------- | ---------------------------------- | ----------- |
| `DD_AGENT_HOST`     | The hostname for the Datadog agent | `localhost` |
| `DD_DOGSTATSD_PORT` | The port for the Datadog agent     | `8125`      |

Start the app with Docker locally:

```sh
docker build -t datadog-sender .
docker run -it -e DD_AGENT_HOST=localhost -e DD_DOGSTATSD_PORT=8125 datadog-sender
```

Run it in Kubernetes using the [deployment manifest](deployment.yaml):

```sh
kubectl apply -f deployment.yaml
```
