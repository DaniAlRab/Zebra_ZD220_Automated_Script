import subprocess
import win32print

# This file will be created
file_path = 'output.txt'

# Read the content of the file and store it in a variable
with open(file_path, 'r') as file:
    content = file.read()

# Function to print raw data to the specified printer
def print_raw(printer_name, data):
    try:
        # Open the printer by name
        printer = win32print.OpenPrinter(printer_name)
        
        # Start a print job
        job_info = win32print.StartDocPrinter(printer, 1, ('Hello Print', None, "RAW"))
        win32print.StartPagePrinter(printer)
        
        # Send raw data to the printer
        win32print.WritePrinter(printer, data.encode('utf-8'))
        
        # End the print job
        win32print.EndPagePrinter(printer)
        win32print.EndDocPrinter(printer)
        
        print("Printed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the printer
        win32print.ClosePrinter(printer)

# Replace 'YourPrinterName' with the name of your Zebra ZD220 printer
printer_name = 'ZDesigner ZD220-203dpi ZPL'

# Set the text to be printed using a variable
text_to_print = "Hello, World! This is a variable text."
 

# Construct ZPL commands with the variable text
zpl_commands = f"""
^XA
^FO20,20^A0N,25,25^FD{content}^FS
^XZ
"""

# Print to the specified printer
print_raw(printer_name, zpl_commands)
# Now 'content' variable holds the content of the file
print(content)  # You can do operations or print to verify the content
subprocess.run(['python', 'imprime_etiqueta_serial_115200_15.2.py'])
