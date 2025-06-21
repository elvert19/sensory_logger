import random
import time
import csv

def get_sensor_data():
    return round(random.uniform(20.0,30.0),2)


def main():
    with open("data.csv","w",newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["Time","sensor Reading(°c)"])

        print(" 🟢 Logging sensor data. Press Ctrl + c to stop.")


        try:
             while True:
                    value = get_sensor_data()
                    timestamp = time.strftime("%H:%M:%S")                        
                    writer.writerow([timestamp, value])
                    print(f"{timestamp} -> {value} °C")
                    time.sleep(2)
        except KeyboardInterrupt:
                   print("🛑 Logging stopped")

    
if __name__ == "__main__":
    main()

