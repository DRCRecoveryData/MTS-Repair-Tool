import os

def repair_mts_file(reference_file, corrupted_file):
    # Read reference file
    with open(reference_file, 'rb') as ref:
        reference_data = ref.read(768)
    
    # Read corrupted file
    with open(corrupted_file, 'rb') as corr:
        corrupted_data = corr.read()
    
    # Replace first 768 bytes of corrupted data with reference data
    repaired_data = reference_data + corrupted_data[768:]
    
    # Get the name of the corrupted file
    filename = os.path.basename(corrupted_file)
    
    # Create directory if not exists
    os.makedirs('Repaired', exist_ok=True)
    
    # Write repaired data to new file with the same name as corrupted file
    with open(os.path.join('Repaired', filename), 'wb') as repaired_file:
        repaired_file.write(repaired_data)

def main():
    reference_file = input("Enter the path to the reference MTS file: ")
    corrupted_file = input("Enter the path to the corrupted MTS file: ")
    repair_mts_file(reference_file, corrupted_file)
    print("Repaired MTS file saved in 'Repaired' folder with the same name as the corrupted file.")

if __name__ == "__main__":
    main()
