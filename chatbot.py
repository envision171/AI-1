def customer_service_bot():
    print("Welcome to our Customer Support Chatbot!")
    print("I can help you with:\n1. Checking your order status\n2. Updating contact information\n3. Support hours\n4. Saying goodbye\n")
    
    while True:
        user_input = input("You: ").strip().lower()

        if "order status" in user_input or "check order" in user_input:
            order_id = input("Please enter your Order ID: ")
            # This is a placeholder response; in a real app, it would check the order database.
            print(f"Chatbot: Checking status for Order ID {order_id}... Your order is being processed.")

        elif "update contact" in user_input or "change contact" in user_input:
            new_contact = input("Please enter your new contact information (email or phone): ")
            # Placeholder response; in a real app, this would update the user's contact info.
            print(f"Chatbot: Your contact information has been updated to {new_contact}.")

        elif "support hours" in user_input or "hours" in user_input:
            print("Chatbot: Our support hours are Monday to Friday, 9 AM to 5 PM.")

        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Thank you for reaching out! Have a great day!")
            break

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can I help with order status, updating contact information, or support hours?")


customer_service_bot()
