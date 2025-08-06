
with open("users.txt", "w") as f:
    f.write("john,1234,5000\n")
    f.write("jane,5678,3000\n")

def load_users():
    users = {}
    with open("users.txt") as file:
        for line in file:
            name, pin, balance = line.strip().split(',')
            users[name] = {"pin": pin, "balance": float(balance)}
    return users

def authenticate(users):
    username = input("Enter username: ")
    pin = input("Enter PIN: ")
    if username not in users:
        raise KeyError("User not found.")
    if users[username]["pin"] != pin:
        raise ValueError("Invalid PIN.")
    return username

def withdraw(users, username):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > users[username]["balance"]:
        raise ValueError("Insufficient funds.")
    users[username]["balance"] -= amount
    print(f"Withdrawal successful. New balance: {users[username]['balance']}")

def atm():
    users = load_users()
    try:
        username = authenticate(users)
        print(f"Welcome {username}!")
        withdraw(users, username)
    except FileNotFoundError:
        print("User database missing!")
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("Transaction completed.")
    finally:
        print("Thank you for using our ATM.")

atm()
