# Configuration

## 1.Golang Configuration

```bash
sudo apt-get install openssl
sudo apt-get install libssl-dev
wget https://studygolang.com/dl/golang/go1.14.3.linux-armv6l.tar.gz
sudo tar -C /usr/local -xzf go1.14.3.linux-armv6l.tar.gz 
```

open .bshrc, write env info to the bottom.

```
export PATH=$PATH:/usr/local/go/bin
export GO111MODULE=on
export GOPROXY=https://goproxy.io
```

then,use "source .bashrc" to configure it.


