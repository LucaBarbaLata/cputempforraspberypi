import subprocess
import time

while True:
    # Run the command and capture the output
    result = subprocess.run(['/usr/bin/vcgencmd', 'measure_temp'], capture_output=True, text=True)
    
    # Extract the temperature value from the output
    temperature = result.stdout.strip().split('=')[1]
    
    # Print the temperature
    print(f"Current temperature: {temperature}")
    
    # Wait for 1 second before running the command again
    time.sleep(1)
