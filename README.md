# Ai-service

## 1. Project 구성
----------------
### 1.1. install

- poetry 설치

```bash
# linux
sudo apt-get install poetry
```
```bash
# mac
brew install poetry
poetry config virtualenvs.in-project true
```

- 소스 받기

```bash
# linux
cd works # change directory to your directory path
git clone https://github.com/sdkim96/ai_service.git
```


```bash
# mac
cd works # change directory to your directory path
git clone https://github.com/sdkim96/ai_service.git
```

- React JS 설치

1. linux

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
sudo vim ~/.bashrc
```

```sh
a

export NVM_DIR="$HOME/.nvm"
[ -s "/usr/local/opt/nvm/nvm.sh" ] && . "/usr/local/opt/nvm/nvm.sh"

esc
:wq!
```

```bash
source ~/.bashrc

nvm install node
nvm install v20.12.0
nvm use v20.12.0
cd ai-service/frontend

npm install
npm run build
```

2. mac

```bash
brew install nvm
sudo vim ~/.zshrc
```

```sh
a

export NVM_DIR="$HOME/.nvm"
    [ -s "$HOMEBREW_PREFIX/opt/nvm/nvm.sh" ] && \. "$HOMEBREW_PREFIX/opt/nvm/nvm.sh" # This loads nvm
    [ -s "$HOMEBREW_PREFIX/opt/nvm/etc/bash_completion.d/nvm" ] && \. "$HOMEBREW_PREFIX/opt/nvm/etc/bash_completion.d/nvm"

esc
:wq!
```

```bash
source ~/.zshrc

nvm install node
nvm install v20.12.0
nvm use v20.12.0
cd ai-service/frontend

npm install
npm run build
```

- FastAPI 설치
```bash
cd ..s
poetry shell
poetry install

python apps/main.py
```
