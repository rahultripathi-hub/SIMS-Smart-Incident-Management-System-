import random
import datetime

# Predefined values
departments = ["Network Support","Application Support","Database Administration","Security","Cloud Services"]
roles = ["Customer","Engineer","Manager"]
incident_titles = [
    "VPN not connecting","Email not syncing","Laptop overheating",
    "Password reset issue","Slow internet speed","Printer not working",
    "Software crash","Mobile app bug","Database timeout","Account locked","Authentication error",
    "MFA error","No audio","Multiple monitors not connecting","Slow operations on laptop",
    "Microsoft 365 error"
]
priorities = ["Low","Medium","High","Critical"]
statuses = ["Open","In Progress","Resolved","Closed"]

# Generate Departments
for dept in departments:
    print(f"INSERT INTO Departments (dept_name) VALUES ('{dept}');")

# Generate Users (200 users)
for i in range(200):
    role = random.choice(roles)
    name = f"User{i}"
    email = f"user{i}@example.com"
    print(f"INSERT INTO Users (name, role, email) VALUES ('{name}', '{role}', '{email}');")

# Generate Customers (100 customers linked to first 100 users)
for i in range(100):
    print(f"INSERT INTO Customers (user_id, company) VALUES ({i+1}, 'Company{i}');")

# Generate Engineers (50 engineers linked to next 50 users)
for i in range(50):
    dept_id = random.randint(1, len(departments))
    print(f"INSERT INTO Engineers (user_id, dept_id, skillset) VALUES ({i+101}, {dept_id}, 'Skillset{i}');")

# Generate Incidents (1000 incidents)
for i in range(1000):
    customer_id = random.randint(1, 100)
    title = random.choice(incident_titles)
    description = f"Auto-generated issue: {title}"
    priority = random.choice(priorities)
    status = random.choice(statuses)
    days_ago = random.randint(1, 30)
    created_at = (datetime.datetime.now() - datetime.timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M:%S')
    resolved_at = (datetime.datetime.now() - datetime.timedelta(days=days_ago - random.randint(0, 5))).strftime('%Y-%m-%d %H:%M:%S')
    print(f"INSERT INTO Incidents (customer_id, title, description, priority, status, created_at, resolved_at) "
          f"VALUES ({customer_id}, '{title}', '{description}', '{priority}', '{status}', '{created_at}', '{resolved_at}');")

# Generate Assignments (500 assignments)
for i in range(500):
    incident_id = random.randint(1, 1000)
    engineer_id = random.randint(1, 50)
    print(f"INSERT INTO IncidentAssignments (incident_id, engineer_id) VALUES ({incident_id}, {engineer_id});")

# Generate Escalations (100 escalations)
for i in range(100):
    incident_id = random.randint(1, 1000)
    reason = "SLA Breach"
    print(f"INSERT INTO Escalations (incident_id, escalated_to, reason) VALUES ({incident_id}, 'Manager', '{reason}');")

# Generate Communications (300 communications)
for i in range(300):
    incident_id = random.randint(1, 1000)
    message = f"Update for incident {incident_id}: Work in progress."
    print(f"INSERT INTO Communications (incident_id, message) VALUES ({incident_id}, '{message}');")

# Generate Knowledge Base entries
for i in range(50):
    title = f"KB Article {i}"
    solution = f"Solution details for issue {i}"
    print(f"INSERT INTO KnowledgeBase (title, solution) VALUES ('{title}', '{solution}');")