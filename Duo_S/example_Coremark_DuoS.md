# RuyiSDK 基础示例

## Coremark（GCC）

创建并激活 ruyi 虚拟环境（GCC）

```
ruyi venv -t toolchain/gnu-plct milkv-duo venv-gnu-plct-duo

. ~/venv-gnu-plct-duo/bin/ruyi-activate
```

验证 GCC 版本

```
riscv64-plct-linux-gnu-gcc -v
```

获取源码并编译 coremark

```
git clone https://github.com/eembc/coremark  
#若无法访问GitHub，使用Gitee镜像替代  
#git clone https://gitee.com/mirrors_eembc/coremark

cd coremark

make CC=riscv64-plct-linux-gnu-gcc XCFLAGS="-mcpu=thead-c906 -static" compile

mv coremark.exe coremark-gcc
```
![gnu-hello](./images/gnu-hello-compile.png)

将 GCC 构建的二进制传输至开发板

```
scp ../coremark-gcc root@192.168.42.1:~
```

返回上级目录并退出 ruyi GCC 虚拟环境

```
cd ..; ruyi-deactivate
```

SSH 连接到开发板并执行编译好的二进制

```
ssh root@192.168.42.1

#如提示Host key verification failed：

#打开当前用户目录下的 .ssh/known_hosts目录，删除192.168.42.1对应行

#登录密码为milkv，提示Are you sure you want to continue connecting时输入yes回车即可

./coremark-gcc

```

![gnu-coremark](./images/gnu-coremark-run.png)

## Coremark（LLVM）

创建并激活 ruyi 虚拟环境（LLVM）

```
ruyi venv -t toolchain/llvm-plct manual --sysroot-from gnu-plct venv-llvm-plct-duo

. ~/venv-llvm-plct-duo/bin/ruyi-activate
```

验证 LLVM 版本

```
clang -v
```

下载源码并编译 coremark（LLVM）

```
git clone https://github.com/eembc/coremark  
#若无法访问GitHub，使用Gitee镜像替代  
#git clone https://gitee.com/mirrors_eembc/coremark

cd coremark; make clean

make CC=clang XCFLAGS="-march=rv64imafdc_xtheadba_xtheadbb_xtheadbs_xtheadcmo_\

xtheadcondmov_xtheadfmemidx_xtheadmac_xtheadmemidx_xtheadmempair_xtheadsync -static" compile

mv coremark.exe coremark-llvm
```

![llvm-hello](./images/llvm-hello-compile.png)

将 GCC 构建的二进制传输至开发板

```
scp ../coremark-llvm root@192.168.42.1:~
```

返回上级目录并退出 ruyi LLVM 虚拟环境

```
cd ..; ruyi-deactivate
```

SSH 连接到开发板并执行编译好的二进制

```
ssh root@192.168.42.1

#如提示Host key verification failed：

#打开当前用户目录下的 .ssh/known_hosts目录，删除192.168.42.1对应行

#登录密码为milkv，提示Are you sure you want to continue connecting时输入yes回车即可

./coremark-llvm

```

![llvm-coremark](./images/llvm-coremark-run.png)

