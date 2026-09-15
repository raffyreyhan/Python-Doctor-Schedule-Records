# Python CRUD Application for Hospital Doctor Management

A Python-based application for managing doctor schedule and doctor records in a hospital. The application provides Create, Read, Update, and Delete (CRUD) operations, as well as search functionality to help hospital staff manage doctor information and schedules efficiently.

## Business Understanding

This project supports hospitals in managing doctor information and schedules in a structured and efficient manner. Centralized doctor data helps authorized hospital staff maintain accurate information regarding doctors, their professional titles, medical departments (poli), room assignments, working days, working hours, and working status.

**Benefits:**

* Improved data accuracy:
Centralized doctor and schedule information helps reduce data inconsistencies and duplicate records.
* Efficient data management:
CRUD operations simplify the process of adding, viewing, updating, and deleting doctor schedule records.
* Faster information retrieval:
Search functionality enables users to quickly find doctor information based on name, poli, status, working day, or working hours.
* Better schedule management:
Accurate information regarding working days, working hours, and room assignments supports daily hospital operations.
* Improved data organization:
Structured doctor records make information easier to maintain, access, and update.

**Target Users:**

This application is designed for hospital administrators, medical administration staff, HR personnel, and authorized hospital staff who are responsible for managing and maintaining doctor information and schedules.

## Features

* **Create:**
    * Add new doctor schedule records to the system.
    * Automatically generate a unique doctor ID using the format DR-0001, DR-0002, and so on.
    * Enter the doctor's name.
    * Select the medical poli from 10 available options.
    * Automatically assign the doctor's gelar and poli telephone number based on the selected poli.
    * Select an available consultation room based on the selected poli and working shift.
    * Automatically set the new doctor's status to Aktif.
    * Select exactly 5 working days from the available days of the week.
    * Select one working shift:
       * 08.00 - 14.00
       * 15.00 - 21.00
    * Allow doctors to share a room only when the room and schedule do not conflict.
    * Automatically set room and schedule information to - or Tidak ada jadwal when a doctor is inactive.
    * Provide confirmation before adding a new doctor record.
* **Read:**
    * Display all registered doctor schedule records.
    * Display doctor information in a clear and structured table.
    * Display information including:
       * Doctor ID
       * Doctor name
       * Professional title
       * Poli
       * Poli telephone number
       * Room
       * Status
       * Working days
       * Working hours
    * Provide a menu to display all doctor records or search for specific records.
* **Update:**
    * Search for a doctor by name before updating the record.
    * Select the target doctor using the automatically generated doctor ID.
    * Modify doctor information such as:
       * Name
       * Poli
       * Room
       * Status
       * Working days
       * Working hours
    * Automatically update the doctor's professional title and poli telephone number when the poli is changed.
    * Maintain the existing doctor ID during the update process.
    * Automatically clear room and schedule information when the doctor's status is changed to Tidak Aktif.
    * Validate room availability to prevent schedule conflicts.
    * Provide confirmation before applying changes.
    * Display a success notification after a successful update.
* **Delete:**
    * Search for a doctor by name before deleting the record.
    * Select the target doctor using the doctor ID.
    * Display the selected doctor's information before deletion.
    * Provide confirmation before permanently deleting the record.
    * Display a success notification after the doctor record has been deleted.
* **Search:**
  The application provides five search criteria:
  *1. By Name*
        * Supports partial name searches.
        * Search is case-insensitive.
        * For example, searching dina can display Dina Maharani.
  *2. By Poli*
        * Select one of the available medical poli.
*3. By Status*
        * Search based on:
            * Aktif
            * Tidak Aktif
*4. By Working Day*
        * Select one of the seven days:
            * Senin
            * Selasa
            * Rabu
            * Kamis
            * Jumat
            * Sabtu
            * Minggu
*5. By Working Hours*
        * Select one of the available shifts:
            * 08.00 - 14.00
            * 15.00 - 21.00
* **Security:**
    * Implement user authentication and authorization mechanisms (if sensitive data is involved) to control access to different CRUD operations.
    * ... (Specify additional security features as needed)
* **Reporting:**
    * Generate reports or summaries based on [Data Entity] data to support [Business Functions] (optional).
    * Export data in various formats (e.g., CSV, Excel) for further analysis (optional).

## Installation

1. **Prerequisites:**
    * Python version (specify the required version)
    * Additional dependencies (list any required packages)

2. **Installation:**
    ```bash
    git clone https://github.com/raffyreyhan/Python-Doctor-Schedule-Records.git
    cd Python-Doctor-Schedule-Records
    pip install -r requirements.txt  # If using a requirements.txt file
    ```

3. **Database Setup (if applicable):**
    Follow specific instructions for configuring your database connection, aligning with the business's chosen database management system.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new doctor schedule record with automatically generated ID and structured professional and       scheduling information.
    * **Read:** Display all registered doctor records and their complete schedule information.
    * **Update:** Modify an existing doctor record while maintaining the existing doctor ID.
    * **Delete:** Remove an existing doctor record after user confirmation.
    * **Search:** Find doctor records using name, poli, status, working day, or working hours.
      
## Data Model
This project uses a structured data model to store hospital doctor and schedule information:
   * **Doctors**
      * id (String, Primary Key):
        Automatically generated unique identifier for each doctor, using the format DR-0001, DR-0002, and so on.
      * nama (String):
        Full name of the doctor.
      * gelar (String):
        Professional medical title automatically determined by the selected poli.
      * poli (String):
        Medical department/poli where the doctor provides medical services.
      * telp (String):
        Telephone number associated with the selected poli. This value is automatically determined based on the selected             poli.
      * ruang (String):
        Consultation room assigned to the doctor. Each poli provides three available rooms.
      * status (String):
        Current working status of the doctor:
            * Aktif
            * Tidak Aktif
      * hari (List/String):
        Working days of the doctor. An active doctor works exactly 5 days per week. For inactive doctors, the value is Tidak         ada jadwal.
      * jam (String):
        Working shift of the doctor:
            * 08.00 - 14.00
            * 15.00 - 21.00
        For inactive doctors, the value is Tidak ada jadwal.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [your_email] or submit an issue if you encounter any problems or have suggestions for improvements.

