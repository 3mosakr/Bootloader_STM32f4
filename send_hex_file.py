import serial

def send_hex_file_line_by_line(file_path, port_name):
    try:
        # Open the serial port
        ser = serial.Serial(port_name, baudrate=9600, timeout=1)
        flag = 0
        # Read the .hex file line by line
        with open(file_path, 'r') as hex_file:
            for line in hex_file:
                # Extract data from each record (string Format)
                bytes_to_send = bytes(line, 'utf-8')
                
                # Send the data along with a colon
                ser.write(bytes_to_send)  # Send the data

                # This helps ensure that each line is sent separately
                ser.flush()  # Flush the output buffer
                # Wait for a short time betwen each record (adjust as needed)
                # time.sleep(0.01)  # Wait for 10 milliseconds
                
                # Wait for 5 seconds in after send first record 
                # (unti MCU erasing the flash section)
                if(flag == 0):
                    time.sleep(5)
                    flag =1

        print(f"Data sent successfully via {port_name}")

        # Close the serial port
        ser.close()
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import time
    file_path = "./file.hex"  # Provide the actual hex file path
    com_port = "COM5"  # Replace with your COM port name
    send_hex_file_line_by_line(file_path, com_port)
