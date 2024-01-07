# hibird_python
本项目展示 Python 混合编程调用 C 语言

演示了以下功能：
1. Python 调用 `*.c` 形式的 C 语言源码
    - 特点：打包的是 c 源码，在使用者执行 `pip install` 时编译，因此可以无视目标机器的操作系统型号
    - c 代码放在 `my_build/core`
2. 如何把 Python/C 编译为 `*.so`，然后被另一个 Python 项目打包。
    - 特点1：可以达到代码加密的效果，因为用户能接触到的是编译后的 `*.so` 文件
    - 特点2：编译过程是在打包时的机器上进行的，未必与用户操作系统一致，从而会产生对应的问题。要解决的话，只能编译多个结果。
    - 待编译的代码放在 `./core_private_source`，编译后，需要手动把 `*.so` 文件放在 `./my_build/core_private` 
    - `setup.py` 中，把 `*.so` 文件以“数据文件”的形式加进去（`package_data`）
3. 把数据文件一起打包。有些项目往往需要带数据文件（比如 txt/csv/jpg）
    - 这样指定：`package_data={'my_build': ['data/*.txt', 'core_private/*.so']},`
4. 作为一个 Python 包，把整个项目打包发布到 pypi.org 
 

Python 调用 C/Rust 有两种打包方法
1. 在开发者的机器上编译，然后用 Python 读取编译后的文件，然后执行它
   - 特点1: 有代码加密的效果，因为用户只能接触到编译后的 `*.so` 文件
   - 特点2: 需要针对用户的不同的操作系统版本编译多个 `*.so` 文件
2. 开发者不编译 setup 把 C/Rust 源文件，而是记录在 `setup.py` 里面，在用户 `pip install xxx` 的时候自动在用户的机器上编译
    - 特点1: 代码是公开的
    - 特点2: 不需要处理多平台编译的问题


如何安装？
```bash
# step1，进入到 ./core_private_source，编译并覆盖到 ./my_build/core_private
# step2:
pip install .
```

## 额外知识点 

多个 `*.c` 文件，且它们之间存在调用关系，如何办？
1. 按照 C 语言的规则整理各个文件，被调用的 `*.c` 文件，需要添加对应的 `*.h` 文件
2. 在 `setup.py` 中，把所有的  `*.c` 文件都列进去，但不要列 `*.h` 文件
 

如果有 `.h` 文件，如何打包？
- 建立文件 `MANIFEST.in`，然后填入文本例如 `include fuzzy_hash/lib/*.h`。打包时就把对应的 `.h` 文件打包进去了
- 【实测不成功】 `Extension(include_dirs=****)` 可以指定头文件所在的目录


更详细的文档 ：https://www.guofei.site/2021/09/12/hybrid.html
