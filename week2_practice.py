# Try typing this out manually instead of copying and pasting!
order_total = 120.00

if order_total >= 100:
    discount = 0.20
elif order_total >= 50:
    discount = 0.10
else:
    discount = 0.0

final_price = order_total * (1 - discount)
print(f"Original: ${order_total} | Final Price: ${final_price}")

# --- PART 2 & 3: Support Tickets & Queue Processing ---

tickets = [
    {"id": 101, "language": "German", "urgency": "high"},
    {"id": 102, "language": "English", "urgency": "low"},
    {"id": 103, "language": "Armenian", "urgency": "high"},
    {"id": 104, "language": "Russian", "urgency": "medium"}
]

supported_languages = set()

print("\n--- Support Queue Processing ---")
for ticket in tickets:
    supported_languages.add(ticket["language"])
    
    if ticket["urgency"] == "high":
        print(f"🚨 Priority Alert: Ticket #{ticket['id']} ({ticket['language']}) escalated!")
    elif ticket["urgency"] == "medium":
        print(f"⚠️ Standard Queue: Ticket #{ticket['id']} ({ticket['language']}) assigned.")
    else:
        print(f"ℹ️ Low Priority: Ticket #{ticket['id']} queued.")

print(f"\nUnique languages active today: {supported_languages}")