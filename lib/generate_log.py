from datetime import datetime
import os

def generate_log(data):
    # log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    if isinstance(data,list):
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")

        print(f"Log written to {filename}")
        return filename
    else : 
        raise ValueError("This should be a list")
