# SemgrepAnalyzer
SemgrepAnalyzer is a powerful and user-friendly tool designed for static code analysis using Semgrep by generating output in HTML. It enables developers and security professionals to scan codebases for vulnerabilities and code issues efficiently.

## Setup tool

```bash
git clone https://github.com/m14r41/SemgrepAnalyzer.git

cd SemgrepAnalyzer

mv semgrepAnalyzer.py semgrepAnalyzer
chmod +x semgrepAnalyzer

sudo mv semgrepAnalyzer /usr/local/bin

cd .. && rm -rf SemgrepAnalyzer
```


---

## Screenshot
![image](https://github.com/user-attachments/assets/685c96bd-152a-46f4-a18d-f247a8fac7e0)


## Aditional 

```bash
# install through pip
python3 -m pip install semgrep

# confirm installation succeeded by printing the currently installed version
semgrep --version

# Login
semgrep login

# Run scan
semgrep ci

semgrep scan --config auto 
