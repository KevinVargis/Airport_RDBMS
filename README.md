The Attached Python CLI uses the sql database stored in DNA_PROJECT.sql 

Attached populate.txt contains all the base data used in population of database, and hence provides data for queries through CLI
Provided Functionalities are Based on the requirements mentioned in phase one of project


**Update Meal Type:**
On entering a valid passenger passport id, and preference of meal type and class, either existing meal is updated, 
or a new meal is created if not already present,

Meal preferences are limited to given options
and are case insensitive.


**Delete passenger:**
Deletes luggage , meal details of passenger as well as removes the passenger from its current flight provided passenger exists in database.

**Add Passenger:**
Checks if flight with given start and end point exists in system, and if flight is not full (<150 current passengers), a ticket number (unique) is assigned , meal preferences assked and a meal booked, and luggage added if required with the constraint that each bag <=30 sq units in volume
Passenger details are also taken in as input and stored
