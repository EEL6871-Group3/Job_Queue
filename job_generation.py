import random

def generate_stress_ng_jobs(num_jobs, file_path):
    # Define ranges for different parameters
    io_range = (1, 16)
    vm_range = (1, 16)
    vm_bytes_range = (1, 8)  # in GB
    timeout_range = (1, 60)  # in minutes

    # Open the file in append mode
    with open(file_path, 'a') as file:
        for _ in range(num_jobs):
            # Randomly select values from the ranges
            io_count = random.randint(*io_range)
            vm_count = random.randint(*vm_range)
            vm_bytes = f"{random.randint(*vm_bytes_range)}G"
            timeout = f"{random.randint(*timeout_range)}m"

            # Format the stress-ng command
            command = f"stress-ng --io {io_count} --vm {vm_count} --vm-bytes {vm_bytes} --timeout {timeout}"
            # Append the command to the file
            file.write(command + "\n")

    return f"Generated {num_jobs} stress-ng jobs and appended to {file_path}"

# Example usage
output_file_path = "job_list.txt"  # Replace with your file path
num_of_jobs = 10  # number of jobs to generate

generate_stress_ng_jobs(num_of_jobs, output_file_path)
