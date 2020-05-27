# 资料及配置指南

## 开发资料

### 树莓派更新 EEPROM 及系统下载

- <https://www.raspberrypi.org/downloads/>

    推荐使用 Raspberry Pi Imager 更新 EEPROM 和烧写镜像，但强烈建议下载好最新版系统镜像，使用该软件的刷入其他 IMG 镜像文件的方式写入，软件自己下载系统镜像的速度太慢。

### 7 寸 HDMI 电阻触摸屏

- <http://www.waveshare.net/wiki/7inch_HDMI_LCD>

### 7 寸 HDMI 电容触摸屏

- <http://www.waveshare.net/wiki/7inch_HDMI_LCD_(H)>

### 树莓派红外相机

- <http://www.waveshare.net/wiki/RPi_NoIR_Camera_V2>

### 光照传感器

- <http://www.waveshare.net/wiki/TSL25911_Light_Sensor>

### 温湿度气压传感器

- <http://www.waveshare.net/wiki/BME280_Environmental_Sensor>

-----

## 系统配置方法

### 树莓派 4B 系统配置方法

- 烧写镜像完成后打开 boot 分区，编辑 config.txt 文件，在文件末尾加上以下内容：

    ```
    # 7 inch HDMI LCD (H) Configurations
    max_usb_current=1
    hdmi_force_hotplug=1 
    config_hdmi_boost=10
    hdmi_group=2 
    hdmi_mode=87 
    hdmi_cvt 1024 600 60 6 0 0 0
    ```

- dtoverlay=vc4-fkms-V3D 的功能是启用 GPU 硬件渲染，注释掉会降低渲染性能且提高功耗。

- 因此，删除以下段落：

    ```
    [all]
    #dtoverlay=vc4-fkms-v3d
    ```

- 修改完毕后保存并退出。

- 安全弹出内存卡。

- 开机启动后在弹出的初始设置界面正常设置，询问是否更新时选择跳过；询问是否重启时选择稍后。

- 从启动菜单选择 Preference -> Raspberry Pi Configuration 项。

- 在 Display 标签页中启用 Overscan 并关闭 Pixel Doubling、Composite Video 和 Screen Blanking 选项。

- 在 Interfaces 标签页中打开全部接口，在 Performance 标签页中设置显存为256MB。

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

### 树莓派 Zero W 系统配置方法（未验证）

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

- 开机启动后在弹出的初始设置界面正常设置，询问是否更新时选择跳过；询问是否重启时选择稍后。

- 从启动菜单选择 Preference -> Raspberry Pi Configuration 项。

- 在 Display 标签页中启用 Overscan 并关闭 Pixel Doubling、Composite Video 和 Screen Blanking 选项。

- 在 Interfaces 标签页中打开全部接口，在 Performance 标签页中设置显存为256MB。

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
    sudo apt update && sudo apt install tree htop git screen tmox net-tools curl wget nano 
    ```

- 执行以下命令安装电阻屏触摸驱动：

    ```
    git clone https://github.com/waveshare/LCD-show.git
    cd LCD-show/
    sudo ./LCD7-1024x600-show
    ```

- 安装完成后重启系统

-----

## 信号接线方式

### 树莓派 4B 接线方式

- 5V 3A Type-C 电源。

- Micro HDMI 转 HDMI 视频信号线使用靠近电源接口的 HDMI0 接口。

- 7 inch HDMI LCD (H) 的触摸信号通过 Micro USB 转 USB-A 电缆连接到树莓派 4B 上的 USB2.0 下层端口。

- 树莓派键盘鼠标套装通过自带的 Micro USB 转 USB-A 电缆连接到树莓派 4B 上的 USB2.0 上层端口。

- 已配置为 USB Ethernet 设备的树莓派 Zero W 通过 Micro USB 转 USB-A 电缆连接到树莓派 4B 上的 USB3.0 下层端口。

- 40 Pin 排针通过排母与洞洞板上的 XH2.54 接口和 KF2510 接口连通。

- 温湿度气压传感器通过 XH2.54 线缆接入树莓派 4B 上的 IIC 接口。

- 光照强度传感器通过 XH2.54 线缆接入树莓派 4B 上的 IIC 接口。

- 12025 排气风扇通过 KF2510 线缆接入树莓派 4B 上的 GPIO 接口。

- MG996R 舵机通过 XH2.54 线缆接入树莓派 4B 上的 GPIO 接口。

- 12V 3W COB LED PWM 调光模块通过 XH2.54 线缆接入树莓派 4B 上的 GPIO 接口。

    共计占用 IIC 地址 2 个和 GPIO 端口 4 个以及 USB 接口 3 个。

### 树莓派 Zero W 接线方式

- 已配置为 USB Ethernet 设备的树莓派 Zero W 通过 Micro USB 转 USB-A 电缆连接到树莓派 4B 上的 USB3.0 下层端口。

- 树莓派 Zero W 通过屏幕背后的插针直接获取 7 inch HDMI LCD 的 SPI 触摸信号。

- 7 inch HDMI LCD 的 HDMI 信号通过 Mini HDMI 转 HDMI 线缆连接树莓派 Zero W 的 Mini HDMI 接口获取。

-----

## 电路接线方式

### 强电部分

- 三脚插头插入三脚插座公口，通过保险丝和开关向箱内供电。

- 将三脚插座母口并接到三脚插座公口保险丝和开关前的位置上。

- 公口插座的开关控制箱内的三孔排插。

- 左右分别是树莓派 5V3A 供电插头和 12V2A 供电插头，中间是小体积双口 5V2A 插头。

### 弱电部分

- 5V3A 专供树莓派。

- 12V2A 通过 5.5*2.1 圆插头和 2P XH2.54 插座接入 KF2510 插座。

- 12V2A 通过 5.5*2.1 圆插头和 2P XH2.54 插座接入 COB LED 模组。

- 5V2A 分两个口供应两个触摸屏的电源。
