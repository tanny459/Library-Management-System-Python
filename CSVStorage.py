import csv

class CSVStorage:
    
    def __init__(self, file_path):
        """
        Initialize CSVStorage object with the file path.

        Args:
            file_path (str): The path to the CSV file.
        """
        self.file_path = file_path

    def load(self):
        """
        Load data from the CSV file.

        Returns:
            list: A list of dictionaries representing the data.
        """
        data = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass
        return data

    def save(self, data):
        """
        Save data to the CSV file.

        Args:
            data (list): A list of dictionaries representing the data to be saved.
        """
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = data[0].keys() if data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
