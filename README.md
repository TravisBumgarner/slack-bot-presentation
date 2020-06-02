# Resources

## Slack

- [Documentation](https://api.slack.com/)
- [Webhooks Documentation](https://api.slack.com/messaging/webhooks#sending_messages)
- [App Directory](https://api.slack.com/apps)
- [Block Kit Builder](https://app.slack.com/block-kit-builder)

## GCP

- [gcloud command line Documentation](https://cloud.google.com/sdk/gcloud/reference)
- [Console](console.cloud.google.com)

# Commands

## Test Webhook

`curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' WEBHOOK_URL_HERE`

## Upload Code to GCP

1. `export APP="slack-bot-presentation";`
2. `gcloud functions deploy $APP --entry-point=main --trigger-topic=$APP --set-env-vars="APP=$APP" --runtime=python37 --timeout=120`
3. `gcloud scheduler jobs create pubsub $APP --schedule="0 * * * *" --topic=$APP --message-body=$APP`