def read_and_write_files():
    try:
       
        input_file = input("Enter the name of the file to read from: ")
        
        
        with open(input_file, "r") as file:
            content = file.readlines()
        
       
        modified_content = ["Modified: " + line for line in content]
        
       
        output_file = input("Enter the name of the file to write to: ")
        
       
        with open(output_file, "w") as file:
            file.writelines(modified_content)
        
        print(f"Modified content written to {output_file} successfully.")
    
    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist.")
    except IOError:
        print("Error: There was a problem reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_files()
