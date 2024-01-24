Application runs on local device to track orders of one cafe branch

# Background information

My client has launched a pop-up cafe in a busy business district. They are offering refreshments to the surrounding offices. They require a software application which helps them to log and track orders.
This order tracking application will allow them to log and track orders using CLI command.

# Client Requirements

As a business:
- They want to maintain a collection of products and couriers.
- When a customer makes a new order, they need to create this on the system.
- They need to be able to update the status of an order
- When they exit the app, all data needs to be persisted and not lost.
- When they start the app, all persisted data will be loaded.

# How to Run the App 

User should have Python installed.

Start using the program by running the program Python file in the terminal.

The program runs on the command line. It has menus of options on display and requests for user input.
User should choose appropriate options and input relevant information where required.
The program has option to exit/ return to main menu to assist user with navigating the program. 

# Program structure

Main Menu:

	0: Save all data and exit the program
	1: Open Product Menu
	2: Open Courier Menu
	3: Open Order Menu

        1: Product Menu:
            0: Return to Main Menu
            1: View Product List
            2: Add New Product to Product List

        2: Courier Menu:
            0: Return to Main Menu
            1: View Courier List
            2: Add New Courier to Courier List

        3: Order Menu:
            0: Return to Main Menu
            1: View existing Order
            2: Create New Order
            3: Update Order Status
