import json
import os


FILE_NAME = "applications.json"


class PlacementTracker:

    def __init__(self):
        self.applications = []
        self.load_data()

    # -------------------------------
    # Load data from JSON file
    # -------------------------------
    def load_data(self):

        if os.path.exists(FILE_NAME):

            try:
                with open(FILE_NAME, "r") as file:
                    self.applications = json.load(file)

            except json.JSONDecodeError:
                print("Data file is corrupted. Starting with empty data.")
                self.applications = []

        else:
            self.applications = []

    # -------------------------------
    # Save data to JSON file
    # -------------------------------
    def save_data(self):

        with open(FILE_NAME, "w") as file:
            json.dump(self.applications, file, indent=4)

    # -------------------------------
    # Add application
    # -------------------------------
    def add_application(self):

        print("\n===== ADD APPLICATION =====")

        company = input("Company name: ").strip()
        role = input("Job role: ").strip()
        location = input("Location: ").strip()

        while True:
            cgpa = input("Your CGPA: ").strip()

            try:
                cgpa = float(cgpa)

                if 0 <= cgpa <= 10:
                    break

                print("CGPA must be between 0 and 10.")

            except ValueError:
                print("Please enter a valid number.")

        status = "Applied"

        application = {
            "id": len(self.applications) + 1,
            "company": company,
            "role": role,
            "location": location,
            "cgpa": cgpa,
            "status": status
        }

        self.applications.append(application)

        self.save_data()

        print("\nApplication added successfully!")

    # -------------------------------
    # View applications
    # -------------------------------
    def view_applications(self):

        print("\n===== ALL APPLICATIONS =====")

        if not self.applications:
            print("No applications found.")
            return

        for application in self.applications:

            print("\n----------------------------")

            print("ID       :", application["id"])
            print("Company  :", application["company"])
            print("Role     :", application["role"])
            print("Location :", application["location"])
            print("CGPA     :", application["cgpa"])
            print("Status   :", application["status"])

    # -------------------------------
    # Search application
    # -------------------------------
    def search_application(self):

        print("\n===== SEARCH APPLICATION =====")

        keyword = input("Enter company or role: ").lower()

        found = False

        for application in self.applications:

            company = application["company"].lower()
            role = application["role"].lower()

            if keyword in company or keyword in role:

                print("\n----------------------------")

                print("ID       :", application["id"])
                print("Company  :", application["company"])
                print("Role     :", application["role"])
                print("Location :", application["location"])
                print("Status   :", application["status"])

                found = True

        if not found:
            print("No matching application found.")

    # -------------------------------
    # Update application status
    # -------------------------------
    def update_status(self):

        print("\n===== UPDATE STATUS =====")

        try:
            application_id = int(input("Enter application ID: "))

        except ValueError:
            print("Invalid ID.")
            return

        for application in self.applications:

            if application["id"] == application_id:

                print("\nAvailable statuses:")
                print("1. Applied")
                print("2. Shortlisted")
                print("3. Interview")
                print("4. Selected")
                print("5. Rejected")

                choice = input("Choose status: ")

                statuses = {
                    "1": "Applied",
                    "2": "Shortlisted",
                    "3": "Interview",
                    "4": "Selected",
                    "5": "Rejected"
                }

                if choice in statuses:

                    application["status"] = statuses[choice]

                    self.save_data()

                    print("Status updated successfully!")

                else:
                    print("Invalid status.")

                return

        print("Application not found.")

    # -------------------------------
    # Delete application
    # -------------------------------
    def delete_application(self):

        print("\n===== DELETE APPLICATION =====")

        try:
            application_id = int(input("Enter application ID: "))

        except ValueError:
            print("Invalid ID.")
            return

        for application in self.applications:

            if application["id"] == application_id:

                self.applications.remove(application)

                self.save_data()

                print("Application deleted successfully!")

                return

        print("Application not found.")

    # -------------------------------
    # Placement statistics
    # -------------------------------
    def statistics(self):

        print("\n===== PLACEMENT STATISTICS =====")

        total = len(self.applications)

        if total == 0:
            print("No applications available.")
            return

        applied = 0
        shortlisted = 0
        interview = 0
        selected = 0
        rejected = 0

        for application in self.applications:

            status = application["status"]

            if status == "Applied":
                applied += 1

            elif status == "Shortlisted":
                shortlisted += 1

            elif status == "Interview":
                interview += 1

            elif status == "Selected":
                selected += 1

            elif status == "Rejected":
                rejected += 1

        print("Total Applications :", total)
        print("Applied            :", applied)
        print("Shortlisted        :", shortlisted)
        print("Interviews         :", interview)
        print("Selected           :", selected)
        print("Rejected           :", rejected)

        success_rate = (selected / total) * 100

        print("Selection Rate     :", round(success_rate, 2), "%")


# =====================================
# MAIN PROGRAM
# =====================================

def main():

    tracker = PlacementTracker()

    while True:

        print("\n")
        print("========================================")
        print("       STUDENT PLACEMENT TRACKER")
        print("========================================")

        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Application")
        print("4. Update Status")
        print("5. Delete Application")
        print("6. Placement Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            tracker.add_application()

        elif choice == "2":
            tracker.view_applications()

        elif choice == "3":
            tracker.search_application()

        elif choice == "4":
            tracker.update_status()

        elif choice == "5":
            tracker.delete_application()

        elif choice == "6":
            tracker.statistics()

        elif choice == "7":
            print("\nThank you for using Placement Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
