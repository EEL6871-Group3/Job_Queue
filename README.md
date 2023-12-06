# Job Generation
## Overview
This Python script generates stress-ng jobs with random parameters based on specified ranges. The generated jobs are appended to a file, creating a job queue for stress testing.

## Source Code Explanation
The source code contains a Python script that takes command-line arguments to define the ranges for stress-ng job parameters. The generated jobs include options for I/O operations (--io), virtual memory stress (--vm and --vm-bytes), and a timeout duration (--timeout). The generated commands are then written to a file, creating a job queue.

## Usage
Execute the script with the following command-line arguments:

bash
python job_generation.py <io_min> <io_max> <vm_min> <vm_max> <vm_bytes_min> <vm_bytes_max> <timeout_min> <timeout_max> <num_of_jobs>
Example:

```bash
python job_generation.py 0 5 0 5 0 4 10 30 30
```
The generated stress-ng commands will be appended to the job_list.txt file by default.
