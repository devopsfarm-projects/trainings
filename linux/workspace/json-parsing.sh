admin_events=$(curl -s https://api.partywalah.in/api/admin/events)
event_names=$(echo "$admin_events" | jq -r '.data[].name.name')
echo $event_names
for name in $event_names; do
    echo "$name"
done