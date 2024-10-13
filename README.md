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

![image](https://github.com/user-attachments/assets/45d5063f-0890-439c-9c70-acfaf537736c)
![image](https://github.com/user-attachments/assets/37516877-89df-426a-84ee-0c04a17546b6)


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
