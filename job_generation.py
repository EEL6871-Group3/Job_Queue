import random
import sys

def generate_stress_ng_jobs(io_range, vm_range, vm_bytes_range, timeout_range, num_jobs, file_path):
    # Open the file in append mode
    with open(file_path, 'a') as file:
        for _ in range(num_jobs):
            # Randomly select values from the ranges
            io_count = random.randint(*io_range)
            vm_count = random.randint(*vm_range)
            vm_bytes = f"{random.randint(*vm_bytes_range)}G"
            timeout = f"{random.randint(*timeout_range)}s"

            # Format the stress-ng command
            command = f"stress-ng --io {io_count} --vm {vm_count} --vm-bytes {vm_bytes} --timeout {timeout}"
            # Append the command to the file
            file.write(command + "\n")

    return f"Generated {num_jobs} stress-ng jobs and appended to {file_path}"

if __name__ == "__main__":
    # Read arguments from the command line
    try:
        io_range = (int(sys.argv[1]), int(sys.argv[2]))
        vm_range = (int(sys.argv[3]), int(sys.argv[4]))
        vm_bytes_range = (int(sys.argv[5]), int(sys.argv[6]))  # in GB
        timeout_range = (int(sys.argv[7]), int(sys.argv[8]))  # in minutes
        num_of_jobs = int(sys.argv[9])
    except IndexError:
        print("Error: Not enough arguments provided.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid argument type. Please provide integer values.")
        sys.exit(1)

    # Set a default output file path
    output_file_path = "job_list.txt"

    result = generate_stress_ng_jobs(io_range, vm_range, vm_bytes_range, timeout_range, num_of_jobs, output_file_path)
    print(result)
