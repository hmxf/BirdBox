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
