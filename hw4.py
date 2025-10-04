def handle_shutdown():
    user_input = input("Do you want to shut down? (yes/no): ").strip().lower()
    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("No shutdown.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

handle_shutdown()
