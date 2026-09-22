import datetime

def log_customer_issue(ticket_id, customer_name, issue_description):
    """Formats and appends a customer ticket to a local file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] TICK-{ticket_id} | Client: {customer_name} | Issue: {issue_description}\n"
    
    try:
        with open("customer_tickets.txt", "a") as file:
            file.write(log_entry)
        return True
    except IOError as e:
        print(f"Failed to write to file: {e}")
        return False

# Simulate processing inputs safely
raw_tickets = [
    {"id": 101, "name": "Anna", "issue": "Payment failed"},
    {"id": 102, "name": "Markus", "issue": "Address correction"},
]

for t in raw_tickets:
    success = log_customer_issue(t["id"], t["name"], t["issue"])
    if success:
        print(f"Successfully logged ticket #{t['id']}")

# Read back and verify
print("\n--- Current Logged File Output ---")
with open("customer_tickets.txt", "r") as file:
    print(file.read())