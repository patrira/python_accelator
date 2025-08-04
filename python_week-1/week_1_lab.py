
def get_valid_name():

    while True:
        name = input("Enter full name: ").strip()
        if name:
            return name.title()
        print("Name cannot be empty.")

def get_valid_age():

    while True:
        age_input = input("Enter age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            if age > 0:
                return age
        print("Invalid age. Please enter a positive number.")

def get_valid_ticket_type():

    while True:
        ticket = input("Enter ticket type (VIP or Regular): ").strip().lower()
        if ticket in ["vip", "regular"]:
            return ticket.upper()
        print("Invalid ticket type. Please enter 'VIP' or 'Regular'.")

def assign_zone(age, ticket):

    if ticket == "VIP":
        return "VIP Zone"
    elif age < 18:
        return "Youth Zone"
    else:
        return "Standard Zone"

def get_attendee_info():

    name = get_valid_name()
    age = get_valid_age()
    ticket = get_valid_ticket_type()
    zone = assign_zone(age, ticket)

    return {
        "name": name,
        "age": age,
        "ticket": ticket,
        "zone": zone
    }

def print_attendee(attendee):

    print("\n Registration Complete!")
    print("-" * 30)
    print(f"Name        : {attendee['name']}")
    print(f"Age         : {attendee['age']}")
    print(f"Ticket Type : {attendee['ticket']}")
    print(f"Seating Zone: {attendee['zone']}")
    print("-" * 30)

def print_summary(attendees):

    print("\n Event Summary:")
    print("-" * 30)

    zone_count = {"VIP Zone": 0, "Youth Zone": 0, "Standard Zone": 0}
    total_age = 0

    for attendee in attendees:
        zone_count[attendee["zone"]] += 1
        total_age += attendee["age"]

    total = len(attendees)
    avg_age = total_age / total if total else 0

    for zone, count in zone_count.items():
        print(f"{zone}: {count} attendee(s)")
    print(f"Average Age : {avg_age:.1f}")
    print("-" * 25)

def main():

    attendees = []
    print("\n Welcome to the Event Registration CLI!\n")

    while True:
        attendee = get_attendee_info()
        attendees.append(attendee)
        print_attendee(attendee)

        more = input("Register another attendee? (y/n): ").strip().lower()
        if more != 'y':
            break

    print_summary(attendees)

if __name__ == "__main__":
    main()
