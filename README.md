# security_and_recovery_final_semester
19120641 - 19120694

# launch
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current Project",
            "type": "python",
            "request": "launch",
            "program": "start.py",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
 
#   .env
$   copy .env.default to .env
$
#   obfurcasted code
$   using https://pyarmor.readthedocs.io/en/latest/ 
$   ```pip install pyarmor```
$   ```pyarmor init --entry=start.py```
$   ```pyarmor build```
$   # run obfuscated code
$   ```cd obfuscate```
$   run ```start.py```

