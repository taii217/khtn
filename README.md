# security_and_recovery_final_semester
## Thành Viên
* 19120641 : Nguyễn Đức Phát Tài
* 19120694 : Phan Lý Châu Trinh

## Đề Tài
* 
* 
*



## Launch
```
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
```
 
## .env
* copy .env.default to .env


## Obfuscasted code
* using https://pyarmor.readthedocs.io/en/latest/ 
* how to obfuscate code
```
pip install pyarmor
pyarmor init --entry=start.py
pyarmor build
```

## Run obfuscated code
* run application by obfuscate 
```
cd obfuscate
start.py
```

