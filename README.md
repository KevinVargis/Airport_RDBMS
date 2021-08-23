## Model Relational Database Management System

This example RDBMS is based on the scenario of a hypothetical airport based in Hyderabad.
The database has been populated with some example values to demonstrate the working of functions. These values have been listed in `population.txt`.
The data stored can be queried and updated through `mysql`, and the functional requirements given in the earlier phases have been implemented with python to provide a simple CLI-based menu interface to run the queries.

**Instructions**

This is on the assumption that the user has already installed the MySQL client.

- Enter the folder
- Open the MySQL CLI
- run `source DNA_PROJECT.sql`
- Now close the MySQL CLI and run `python3 kode.py`

**Functional Requirements**

- View all out-going flights on a particular day
    - Takes a valid date value as input

- View all airlines with more than a given number of flights on a particular day
    - Takes a valid date value as input

- Show city with most incoming flights

- Display passenger details search using PASSPORT ID
    - Accepts a string to search for in the PASSPORT_ID set

- Display number of flights with below average number of passengers
    - Displays average number of passengers per flight and details of the required flights

- Show airline flying the highest number of minors

- Add a new passenger to a flight
    - Takes in PASSPORT_ID and other required details needed to make a reservation
    - Checks for flight availibility, luggage constraints, etc.
    - Creates the associated relations such as FLIES_ON, SUPPLIES_TO, etc.

- Update Meal Type:
    - On entering a valid passenger passport id, and preference of meal type and class, either existing meal is updated, or a new meal is created if not already present,
    - Meal preferences are limited to given options and are case insensitive.


- Delete passenger:
    - Deletes luggage , meal details of passenger as well as removes the passenger from its current flight provided passenger exists in database.
