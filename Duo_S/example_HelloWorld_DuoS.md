# RuyiSDK 基础示例

## Hello World (GCC) 

创建并激活 ruyi 虚拟环境（GCC）

```
ruyi venv -t toolchain/gnu-plct milkv-duo venv-gnu-plct-duo

. ~/venv-gnu-plct-duo/bin/ruyi-activate
```

验证 GCC 版本

```
riscv64-plct-linux-gnu-gcc -v
```

编译 Hello World（GCC）

```
cat << EOF > hello.c

#include <stdio.h>

int main() {

printf("Hello, World!\n");

return 0;

}

EOF

riscv64-plct-linux-gnu-gcc hello.c -static -o hello-gcc
```

![gnu-hello](./images/gnu-hello-compile.png)

将 GCC 构建的二进制传输至开发板

```
scp ../hello-gcc root@192.168.42.1:~
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

./hello-gcc

```


![gnu-hello](./images/gnu-hello-run.png)
## Hello World (LLVM) 

创建并激活 ruyi 虚拟环境（LLVM）

```
ruyi venv -t toolchain/llvm-plct manual --sysroot-from gnu-plct venv-llvm-plct-duo

. ~/venv-llvm-plct-duo/bin/ruyi-activate
```

验证 LLVM 版本

```
clang -v
```

编译并运行 Hello World（LLVM）

```
clang hello.c -static -o hello-llvm
```

![llvm-hello](./images/llvm-hello-compile.png)

将 LLVM 构建的二进制传输至开发板

```
scp ../hello-gcc root@192.168.42.1:~
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

./hello-llvm

```

![llvm-hello](./images/llvm-hello-run.png)
