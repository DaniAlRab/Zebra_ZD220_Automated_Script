import subprocess
import serial

# Replace '/dev/ttyUSB0' with your serial port and 9600 with your baud rate
ser = serial.Serial('COM6', 115200)  # Adjust baud rate and com port if needed
file_path = 'output.txt'

# Function to remove characters from the end of the line
def remove_characters(line, num_chars):
    if num_chars > 0:
        return line[:-num_chars]
    return line

try:
    last_received_data = ""  # Variable to store the last received line
    chars_to_remove = 7  # Number of characters to remove from the end of the line
    print("Plugue a placa na Porta Serial COM6, 115200")
    print("")
    print("Verifique se a impressora Zebra ZD220 esta conectada e ligada")
    print("")
    print("Pressione as teclas CTRL+C e desplugue a placa para imprimir")
    print("")

    while True:
        try:
            # Read a line from the serial port and decode it using UTF-8 encoding
            received_data = ser.readline().decode('utf-8', errors='ignore').strip()

            # Update the last received line
            if received_data:
                last_received_data = received_data

            # Remove specified characters from the end of the last received line
            formatted_data = remove_characters(last_received_data, chars_to_remove)

            # Display the formatted last received line
            print("", formatted_data)
            
            substring = formatted_data[:-3]  # Retrieves characters from the 6th character from the end to the 2nd character from the end
            print()  # Output will 

        except UnicodeDecodeError:
            # Handle decoding errors (ignored in this example)
            pass

except KeyboardInterrupt:

    file = open(file_path, 'w')
    file.write("      ")
    file.write(formatted_data)
    file.close()
    ser.close()
    subprocess.run(['python', 'zebra_etiqueta_python.py'])
    print("Serial connection closed.")
