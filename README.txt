HealthNet by HackStreet

HealthNet is a software solution to manage all health data and interactions between nurses, patients, and doctors.

This software solution is optimized for maximum user fluidity and, therefore, we have provided a simple approach.
Any patron with any range of technical experience can use HealthNet and all of its features.

HealthNet provides many administrator and system options for more advanced users.

To run HealthNet, the user must be using Django 1.8.3, Python 3.4.3, and have web access.


Installation:
    Unzip the file in the desired directory.
    Open command prompt, and navigate to the healthNet folder.
        To know you're in the right folder, run the 'dir' command in a windows based system or 'ls' in a unix based system.
        You should see several folders as well as a few files. The files would include '__init__.py', 'db.sqlite3',
        and 'manage.py'.
        That will mean you are in the correct directory.
    Run the following commands.
        python manage.py makemigrations
        python manage.py migrate

    Known Bugs:
        The missing features.
        All users have the same universal access to system log and statistics.

Known Missing Features in Release-2Beta:
    Many features not implemented.
        Messaging
        Appointments

Execution and instructions:
    To access the features of HealthNet, open command line. Change the working directory to the healthNet folder.
    From there, run the next command.
        python manage.py runserver
    Open a web browser, and go to "localhost:8000". From there, you can log in or register.

    Logging in:
        Patient Login:
            username: patient@patient.com
            password: patient
        Doctor Login:
            username: doctor@doctor.com
            password: doctor
        Nurse Login:
            username: nurse@nurse.com
            password: nurse
        Administrator Login:
            username: admin@admin.com
            password: admin