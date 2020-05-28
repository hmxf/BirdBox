# Golang 编译环境配置方法

- 使用以下命令安装必需的库环境：

    ```
    sudo apt-get install openssl libssl-dev
    ```

- 使用以下命令下载适用于树莓派 4B 的 Golang 安装包：

    ```
    wget https://studygolang.com/dl/golang/go1.14.3.linux-armv6l.tar.gz
    ```

- 解压到 /usr/local 路径下：

    ```
    sudo tar -C /usr/local -xzf go1.14.3.linux-armv6l.tar.gz 
    ```

- 将以下内容写入 ~/.bashrc 文件

    ```
    export PATH=$PATH:/usr/local/go/bin
    export GO111MODULE=on
    export GOPROXY=https://goproxy.io
    ```

- 关闭并重新开启终端使改动生效，或者使用以下命令立即生效：

    ```
    source ~/.bashrc
    ```
