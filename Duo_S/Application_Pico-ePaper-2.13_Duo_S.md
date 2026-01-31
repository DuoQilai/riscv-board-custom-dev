# 在 Duo S 上使用 Pico-ePaper-2.13 显示屏

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
    - Pico-ePaper-2.13 显示屏
    - USB 电源适配器
    - USB-A to C 或 USB C to C 线缆
    - microSD 卡
    - USB to UART 调试器
    - 杜邦线

## 工作原理

使用 SPI 通信接口，采用“微胶囊电泳显示”技术进行图像显示，其基本原理是悬浮在液体中的带电纳米粒子受到电场作用而产生迁移。电子纸显示屏是靠反射环境光来显示图案的，不需要背光，在环境光下，电子纸显示屏清晰可视，可视角度几乎达到了 180°。因此，电子纸显示屏非常适合阅读。

## 硬件接线

![Pico-ePaper1-2.13](./images/Pico-ePaper1-2.13.webp)

| 连接名称 | GND  | VCC        | DC    | CS    | RST   | BUSY  | CLK   | DIN   |
| -------- | ---- | ---------- | ----- | ----- | ----- | ----- | ----- | ----- |
| 引脚     | GND  | VCC (3.3V) | PIN50 | PIN11 | PIN13 | PIN46 | PIN23 | PIN19 |

![2.13英寸 LCD Pico 扩展板引脚排列介绍](./images/Pico-ePaper-2.13-details-inter.jpg)

***注意：连接杜邦线时不要参考显示屏的丝印，它的标注很容易让人连接错，请参考引脚图连接***

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

## 编译与运行

```bash
git clone https://github.com/zwyzwm/Pico-ePaper-2.13.git
cd Pico-ePaper-2.13/Pico-ePaper-2.13/c  
make
```

将生成的 `paper` 二进制文件传输至开发板并运行：

```bash
scp -O paper root@192.168.42.1:/root/
ssh root@192.168.42.1
./paper
```

![Running Test](./images/image-20250511160733556.png)

## 预期结果

1. **环境搭建成功**：成功配置交叉编译环境，工具链正常工作。
2. **程序编译顺利**：成功编译出适用于 RISC-V 架构的 `paper` 二进制文件。
3. **显示功能正常**：运行程序后，电子纸屏幕能够刷新并正确显示内容。

## 实际结果

1. **编译环境**：交叉编译链配置完成。
2. **编译产物**：成功生成了目标执行文件。
3. **屏幕显示**：电子纸屏幕刷新正常，内容显示清晰，符合预期。

## 测试结论

测试成功。
