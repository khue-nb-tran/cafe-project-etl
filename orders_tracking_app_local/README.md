# khue-miniproject
# Project Background

My client has launched a pop-up cafe in a busy business district. They are offering refreshments to the surrounding offices. They require a software application which helps them to log and track orders.
This project aims to provide them with this software that allows them to log and track orders using CLI command.

# Client Requirements

As a business:
- They want to maintain a collection of products and couriers.
- When a customer makes a new order, they need to create this on the system.
- They need to be able to update the status of an order
- When they exit the app, all data needs to be persisted and not lost.
- When they start the app, all persisted data will be loaded.
- They need to be sure that the app has been tested and proven to work well.
- They need to receive regular software updates.

# How to Run the App

User should have Python installed.

Start using the program by running the program Python file in the terminal.

The program runs on the command line. It has menus of options on display and requests for user input.
User should choose appropriate options and input relevant information where required.
The program has option to exit/ return to main menu to assist user with navigating the program. 

Program structure:

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

# Project reflection:

My program design met the project's requirements on these aspects:
- Client can maintain a collection of products and couriers.
- When a customer makes a new order, the client can create this on the system.
- They can update status of existing order.
- When they exist the app, all data is persisted to CSV files and not lost.
- When they start the app, all persisted data is loaded.

I guaranteed the project's requirements by prioritize ensuring the core functions of the program which the client wants to be working (e.g: load and persist data; create new products, couriers and orders). I ran the program numerous times going through all the available options to ensure they are working as give the expected results.

If I had more time, I would improve on adding more functional options to the program by doing the STRETCH goals that works with CSV files. I currently have a version of the program with full functional options that only works with TXT files. 

I enjoyed implementing persisting data to external files. Despites the complication of the process, seeing the data got transferred to external files was very exciting.
