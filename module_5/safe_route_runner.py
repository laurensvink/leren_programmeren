import subprocess
import sys

answers = ['b', 'n', 'b', 'b', 'n', 'b', 'b', '1742']

# Run the game and send answers interactively
proc = subprocess.Popen(
    [sys.executable, 'deel 1 Code analyseren/play.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    cwd=r'c:\school\code\leren_programmeren\module_5'
)

# Send all answers at once
input_data = '\n'.join(answers)
stdout, stderr = proc.communicate(input=input_data)

print(stdout)
if stderr:
    print("STDERR:", stderr)
