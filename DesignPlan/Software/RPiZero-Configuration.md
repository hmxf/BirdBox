## 系统配置方法

### 树莓派 Zero W 系统配置方法

- 烧写镜像完成后打开 boot 分区，编辑 config.txt 文件，在文件末尾加上以下内容：

    ```
    # 7 inch HDMI LCD Configurations
    max_usb_current=1
    hdmi_group=2
    hdmi_mode=87
    hdmi_cvt 1024 600 60 6 0 0 0

    # Enable USB Ethernet Function
    dtoverlay=dwc2
    ```

- dtoverlay=vc4-fkms-V3D 的功能是启用 GPU 硬件渲染，注释掉会降低渲染性能且提高功耗。

- 因此，删除以下段落：

    ```
    [all]
    #dtoverlay=vc4-fkms-v3d
    ```

- 修改完毕后保存并退出。

- 编辑 cmdline.txt 文件，找到 rootwait 并在后面插入内容使其成为如下所示的效果：

    ```
    ······ rootwait modules-load=dwc2,g_ether quiet ······
    ```

- 该文件所有内容均在一行，切记不要输入换行符。修改完毕后保存并退出。

- 安全弹出内存卡。

- 连接好键盘鼠标，稍后配置 WiFi 信息。

- 开机启动后在弹出的初始设置界面正常设置，询问是否联网时连接 WiFi，询问是否更新时选择跳过，询问是否重启时选择稍后。

- 从启动菜单选择 Preference -> Raspberry Pi Configuration 项。

- 在 Display 标签页中启用 Overscan 并关闭 Pixel Doubling和 Screen Blanking 选项。

- 在 Interfaces 标签页中打开全部接口，在 Performance 标签页中设置显存为 128MB。

- 点击下方 Overlay File System 右侧的 Configure 按钮，在弹出的页面中为 Overlay 选项选择 Disable 并为 Boot Partition 选项选择 Read Write 选项。

- 连续点击两次 OK 确认并重启系统。

- 打开并编辑 /etc/apt/sources.list 文件，将其中的内容替换为以下内容：

    ```
    # 编辑 `/etc/apt/sources.list` 文件，删除原文件所有内容，用以下内容取代：
    deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi
    #deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi
    ```

- 打开并编辑 /etc/apt/sources.list.d/raspi.list 文件，将其中的内容替换为以下内容：

    ```
    # 编辑 `/etc/apt/sources.list.d/raspi.list` 文件，删除原文件所有内容，用以下内容取代：
    deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui
    ```

- 执行以下命令更新系统并安装常用软件：

    ```
    sudo apt update && sudo apt upgrade && sudo apt autoremove
    sudo apt update && sudo apt install tree htop git screen tmux net-tools curl wget nano
    sudo apt install i2c-tools
    ```

- 执行以下命令安装电阻屏触摸驱动：

    ```
    git clone https://github.com/waveshare/LCD-show.git
    cd LCD-show/
    sudo ./LCD7-1024x600-show
    ```

- 执行以下命令手动更新 wiringPi 到最新版，否则无法支持树莓派 4B：

    ```
    wget https://project-downloads.drogon.net/wiringpi-latest.deb && chmod +x wiringpi-latest.deb
    sudo dpkg -i wiringpi-latest.deb
    ```

- 安装完成后重启系统

- 执行以下命令确认所需要的软件及其版本：

    ```
    which python && python -V && which python3 && python3 -V && gpio -v && gpio readall && i2cdetect -y 1
    ```