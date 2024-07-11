import csv
import os

def clear_student_data(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    # Read the header
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)

    # Write only the header back to the file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
    print(f"All data in {file_path} has been deleted, but headers are retained.")
