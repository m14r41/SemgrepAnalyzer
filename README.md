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
![image](https://github.com/user-attachments/assets/3cae423d-2203-4334-a616-f370703dc2cc)
![image](https://github.com/user-attachments/assets/e6afb766-e42a-468a-9068-33a8acea5fe0)
![image](https://github.com/user-attachments/assets/6474b0c6-dbf9-4fc0-80c7-a12e01c15889)


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
