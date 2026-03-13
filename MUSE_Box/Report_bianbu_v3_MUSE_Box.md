# bianbu (v3) MUSE Box 系统版本和工具链测试报告

## 测试环境

### 操作系统信息

- 系统版本：bianbu v3.0.1
- 系统状态：已完成烧录并可正常启动，终端登录流程验证通过


### 硬件信息

- MUSE Box

  - 设备照片

  - 设备型号截图

    ![device-model](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/device-model.png)

  - 系统信息截图

    ![device-cpuinfo](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/device-cpuinfo.png)

- 键盘、显示器各一台

- 网线、电源适配器

- 若使用Wi-Fi连接，需安装随附的两根天线


## 工具链测试

安装依赖包

```bash
sudo apt update; sudo apt install -y wget tar zstd xz-utils git build-essential
```

安装ruyi包管理器

```bash
wget https://mirror.iscas.ac.cn/ruyisdk/ruyi/tags/0.40.0/ruyi-0.40.0.riscv64

chmod +x ruyi-0.40.0.riscv64

sudo cp -v ruyi-0.40.0.riscv64 /usr/local/bin/ruyi
```

安装GCC和LLVM工具链

```bash
ruyi update

ruyi install gnu-plct llvm-plct
```

### GCC测试

创建并激活ruyi虚拟环境（GCC）

```bash
ruyi venv -t toolchain/gnu-plct manual venv-gnu-plct

. ~/venv-gnu-plct/bin/ruyi-activate
```

验证GCC版本

```bash
riscv64-plct-linux-gnu-gcc -v
```

编译并运行Hello World（GCC）

```bash
cat << EOF > hello.c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
EOF

riscv64-plct-linux-gnu-gcc hello.c -o hello-gcc
./hello-gcc
```

![gnu-hello-compile](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/gnu-hello-compile.png)

![gnu-hello-run](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/gnu-hello-run.png)


编译并运行coremark（GCC）

```bash
git clone https://github.com/eembc/coremark
cd coremark

make CC=riscv64-plct-linux-gnu-gcc XCFLAGS="-march=rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_\
zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt" compile

./coremark.exe
```

![gnu-coremark-compile](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/gnu-coremark-compile.png)

![gnu-coremark-run](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/gnu-coremark-run.png)


返回上级目录并退出ruyi GCC虚拟环境

```bash
cd ..; ruyi-deactivate
```

### LLVM测试

创建并激活ruyi虚拟环境（LLVM）

```bash
ruyi venv -t toolchain/llvm-plct manual --sysroot-from gnu-plct venv-llvm-plct

. ~/venv-llvm-plct/bin/ruyi-activate
```

验证LLVM版本

```bash
clang -v
```

编译并运行Hello World（LLVM）

```bash
clang hello.c -o hello-llvm; ./hello-llvm
```

![llvm-hello-compile](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/llvm-hello-compile.png)

![llvm-hello-run](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/llvm-hello-run.png)


编译coremark（LLVM）

```bash
cd coremark; make clean; make CC=clang XCFLAGS="-march=rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_\
zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt" compile

./coremark.exe
```

![llvm-coremark-compile](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/llvm-coremark-compile.png)

![llvm-coremark-run](https://github.com/zhiyao310/riscv-board-custom-dev/blob/main/MUSE_Box/images/llvm-coremark-run.png)


返回上级目录并退出ruyi GCC虚拟环境

```bash
cd ..; ruyi-deactivate
```

## 完整测试过程

屏幕录制

[![asciicast](https://asciinema.org/a/777476.svg)](https://asciinema.org/a/777476)

## 预期结果

在本次测试中，预期达到以下成果：

1. **RuyiSDK 编译环境可用**  
   在目标系统中成功安装必要的系统依赖（如 `build-essential`、`git`、`wget` 等），完成 Ruyi 包管理器（v0.40.0）的安装，并通过 Ruyi 正常安装 `gnu-plct` 与 `llvm-plct` 工具链。

2. **GCC 工具链功能验证**  
   成功创建并激活 GCC 虚拟环境，能够正确识别 GCC 版本；使用 GCC 工具链完成 Hello World 程序的编译与运行，并完成 Coremark 基准测试的编译与运行，输出符合预期结果。

3. **LLVM 工具链功能验证**  
   成功创建并激活 LLVM 虚拟环境，能够正确识别 Clang 版本；使用 LLVM 工具链完成 Hello World 程序的编译与运行，并完成 Coremark 基准测试的编译与运行，输出符合预期结果。

4. **测试流程完整**  
   测试完成后可正常退出虚拟环境，所有操作步骤可追溯、可复查

## 实际结果

本次测试实际取得的成果如下：

1. **RuyiSDK 环境部署结果**  
   系统依赖包安装完成，Ruyi 包管理器（v0.40.0）安装成功；通过 Ruyi 包管理器成功安装 `gnu-plct` 与 `llvm-plct` 工具链，相关命令执行无报错，环境配置完成。

2. **GCC 工具链测试结果**  
   GCC 虚拟环境创建与激活成功，GCC 版本信息可正确获取；Hello World 程序可正常编译并在开发板上运行；Coremark 基准测试可成功编译并运行，输出结果符合预期。

3. **LLVM 工具链测试结果**  
   LLVM 虚拟环境创建与激活成功，Clang 版本信息可正确获取；Hello World 程序编译、运行成功，准确输出「Hello, World!」；Coremark 基准测试编译、运行成功，输出结果符合预期。

4. **测试流程完成情况**  
   所有测试步骤执行完成后，虚拟环境可正常退出，测试流程与操作步骤已通过截图与录屏方式记录，测试结果可追溯、可复查。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
