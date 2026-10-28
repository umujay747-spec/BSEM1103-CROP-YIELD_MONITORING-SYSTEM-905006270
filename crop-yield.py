from models import CropRecord, CropMonitoringSystem

from input_handler import (
    get_menu_choice,
    get_new_crop_details,
    get_non_empty_text,
    get_update_details
)

from output_handler import (
    show_menu,
    show_message,
    show_record,
    show_records,
    show_record_count
)


def create_sample_records(system):
    """Create sample crop records for testing."""

    sample_records = [
        CropRecord("CR001", "Rice", 2.0, 1800, 1650, "Harvested"),
        CropRecord("CR002", "Cassava", 1.5, 2200, 0, "Growing"),
        CropRecord("CR003", "Maize", 1.0, 900, 750, "Harvested")
    ]

    for record in sample_records:
        system.add_record(record)


def main():
    """Control the main program."""

    system = CropMonitoringSystem()

    create_sample_records(system)

    show_message("=" * 45)
    show_message(CropMonitoringSystem.system_name())
    show_message("=" * 45)

    while True:

        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            show_records(system)

        elif choice == "2":
            new_record = get_new_crop_details()

            if system.add_record(new_record):
                show_message("Crop record added successfully.")
            else:
                show_message("A record with that ID already exists.")

        elif choice == "3":
            record_id = get_non_empty_text(
                "Enter the record ID to search for: "
            )

            record = system.find_record(record_id)
            show_record(record)

        elif choice == "4":
            record_id, actual_yield, status = get_update_details()

            if system.update_record(record_id, actual_yield, status):
                show_message("Crop record updated successfully.")
            else:
                show_message(
                    "Record not found or yield value is invalid."
                )

        elif choice == "5":
            show_record_count(system)

        elif choice == "0":
            show_message(
                "Thank you for using the Crop Yield Monitoring System."
            )
            break

        else:
            show_message(
                "Invalid option. Please choose a number from the menu."
            )


if __name__ == "__main__":
    main()