# 在 Duo S 上使用 Pico-8SEG-LED 数码管

## 测试环境

### 操作系统信息

- 系统版本：Debian v1.6.35
- 下载链接：<https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.35>
- 参考安装文档：<https://github.com/scpcom/sophgo-sg200x-debian>

### 硬件信息

- 开发板：Milk-V Duo S (512M, SG2000)
	- 设备型号截图![device-model](./images/device-model.png)
	- 系统信息截图![device-cpuinfo](./images/device-cpuinfo.png)
- 其他硬件：
    - Pico-8SEG-LED 数码管
    - USB 电源适配器
    - USB-A to C 或 USB C to C 线缆
    - microSD 卡
    - USB to UART 调试器
    - 杜邦线

## 工作原理

使用 SPI 通信接口，74HC595 芯片，包含一个 8 位串行输入与并行输出移位寄存器并提供一个 8 位 D 型存储寄存器，该存储寄存器具有 8 位 3 三态输出。分别提供独立的时钟信号给移位寄存器和存储寄存器，移位寄存器具有直接清零功能和串行输入输出功能以及级联应用（采用标准引脚）。移位寄存器和存储寄存器均为使用正边缘时钟触发，如果这两个时钟连接在一起，移位寄存器始终在存储寄存器的前一个时钟脉冲。所有输入端口均设有防静电及瞬间过压保护电路。

## 硬件连接

Pico-8SEG-LED 引脚图：

![Pico-8SEG-LED](./images/Pico-8SEG-LED.webp)

![duos-pinout-v1.1](./images/duos-pinout-v1.1.webp)

| 连接名称 | VSYS | GND  | RCLK  | CLK   | DIN   |
| -------- | ---- | ---- | ----- | ----- | ----- |
| 连接引脚 | 3.3V | GND  | PIN50 | PIN23 | PIN19 |

| Pico-8SEG                       | 信号     | Milk-V Duo S       |
| ------------------------------- | -------- | ------------------ |
| VSYS（39脚）                    | 3.3V供电 | J3头部 1脚（3.3V） |
| GND（任选，比如3、8、13、18脚） | 地       | J3头部 6脚（GND）  |
| GP9（12脚）                     | RCLK     | J4头部 50脚        |
| GP10（14脚）                    | CLK      | J3头部 23脚        |
| GP11（15脚）                    | DIN      | J3头部 19脚        |

![connection-1](./images/image-20250426174905950.png)

![connection-2](./images/image-20250426174927503.png)

## 搭建运行环境

参考：<https://github.com/milkv-duo/duo-examples>

```bash
git clone https://github.com/milkv-duo/duo-examples.git
cd duo-examples
source envsetup.sh
```

加载编译环境时需要按提示输入所需编译目标：

```bash
Select Product:
1. Duo (CV1800B)
2. Duo256M (SG2002) or DuoS (SG2000)
```

选择 `2`。由于 Duo S 支持 RISCV 和 ARM 两种架构，还需要按提示继续选择：

```bash
Select Arch:
1. ARM64
2. RISCV64
Which would you like:
```

选择 `2` (RISCV64)。

设置交叉编译工具链环境变量：

```bash
# 1. 设置交叉编译工具链前缀
export TOOLCHAIN_PREFIX=/path/to/duo-examples/host-tools/gcc/riscv64-linux-x86_64/bin/riscv64-unknown-linux-gnu-

# 2. 设置编译参数
export CFLAGS="-march=rv64imafdc -mabi=lp64d -O2"

# 3. 设置链接参数
export LDFLAGS="-march=rv64imafdc -mabi=lp64d"
```

## 编译运行

```bash
git clone https://github.com/zwyzwm/Pico-8SEG-LED.git
cd Pico-8SEG-LED/Pico-8SEG-LED/c
make
```

将生成的 `shu` 二进制文件传输至开发板并运行：

```bash
scp -O shu root@192.168.42.1:/root/
ssh root@192.168.42.1
./shu
```

## 预期结果

1. **环境搭建成功**：成功克隆 `duo-examples` 并配置好交叉编译环境。
2. **源码编译成功**：成功克隆 `Pico-8SEG-LED` 源码并编译生成 `shu` 二进制文件。
3. **功能验证通过**：数码管能够正常显示并实现 0000-9999 循环计数。

## 实际结果

1. **环境搭建结果**：交叉编译环境配置正常，工具链可识别。
2. **源码编译结果**：源码编译顺利，生成了目标 RISC-V 架构二进制文件。
3. **功能验证结果**：数码管按预期进行计数显示，SPI 通信正常。

## 测试结论

测试成功。
