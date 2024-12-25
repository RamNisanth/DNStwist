import subprocess
import openpyxl

def get_whois_with_dnstwist(domain):
    print("inside the whois")
    try:
        # Construct the command to run
        command = f'dnstwist -w {domain} | findstr /c:"{domain}"'

        # Use shell=True to process the pipeline correctly on Windows
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True,  # Required for using pipes on Windows
            check=True
        )
        return(result.stdout)
    except subprocess.CalledProcessError as e:
        return(f"Error occurred: {e.stderr}")
    


def save_data_to_excel(data: str, output_file: str):
    print("inside the save to excel")
    # Split the data into rows
    rows = data.splitlines()
    
    # Create a new Excel workbook and sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Domain Data"

    # Define the header row
    headers = ["Type", "Domain", "IP Address", "Registrar", "Creation Date"]
    ws.append(headers)

    # Iterate over each row in the data and split it into columns
    for row in rows:
        # Split the row by whitespace, the first column is "Type", second is "Domain", etc.
        columns = row.split()
        
        # Extract and handle the data
        domain_type = columns[0]  # Type (original, insertion, etc.)
        domain = columns[1]       # Domain name
        ip_address = columns[2]   # IP Address
        registrar = " ".join(columns[3:columns.index("CREATED:")]) if "CREATED:" in columns else ""
        creation_date = columns[-1] if "CREATED:" in columns else ""
        
        # Append the row to the Excel sheet
        ws.append([domain_type, domain, ip_address, registrar, creation_date])

    # Save the workbook to the specified file
    wb.save(output_file)

    





