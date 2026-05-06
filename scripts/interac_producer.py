import json
import time
import random
from azure.eventhub import EventHubProducerClient, EventData

# ── Connection Details ──────────────────────────────────────
CONNECTION_STRING = "Endpoint=sb://esehblt1uh9hw1ztsxwwkg.servicebus.windows.net/;SharedAccessKeyName=key_a6bd21bc-a3a0-4342-938b-4877c61f6ddd;SharedAccessKey=+CqHWNGkvh7uc61XYsEznOnqBbhJHBE3V+AEhKnSIFs=;EntityPath=esehblt1uh9hw1ztsxwwkg_eh"
EVENT_HUB_NAME    = "esehblt1uh9hw1ztsxwwkg_eh"

# ── File paths ──────────────────────────────────────────────
FILES = [
    r"C:\Users\Owner\Downloads\interac_datasets\streaming\real_time_transactions.json",
    r"C:\Users\Owner\Downloads\interac_datasets\streaming\fraud_alert_events.json",
    r"C:\Users\Owner\Downloads\interac_datasets\streaming\etransfer_events.json",
    r"C:\Users\Owner\Downloads\interac_datasets\streaming\cardholder_activity_events.json"
]

# ── Load all events from all files ─────────────────────────
all_events = []
for file_path in FILES:
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                all_events.append(json.loads(line))

print(f"Total events loaded: {len(all_events):,}")

# ── Shuffle so all event types are mixed ───────────────────
random.shuffle(all_events)

# ── Send events to Eventstream ─────────────────────────────
producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING,
    eventhub_name=EVENT_HUB_NAME
)

print(f"Starting to send events...")
print(f"Press Ctrl+C to stop\n")

sent = 0
batch_size = 10

with producer:
    for i in range(0, len(all_events), batch_size):
        batch_events = all_events[i:i + batch_size]
        event_data_batch = producer.create_batch()

        for event in batch_events:
            event_data_batch.add(EventData(json.dumps(event)))

        producer.send_batch(event_data_batch)
        sent += len(batch_events)

        print(f"Sent: {sent:,} / {len(all_events):,} events", end="\r")
        time.sleep(0.5)

print(f"\nCompleted. Total events sent: {sent:,}")