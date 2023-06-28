# hibird_python
本项目展示 Python 如果混合编程

展示如何同时实现以下功能
1. Python 如何调用 `*.c` 形式的 C 语言。
    - 特点：不用管操作系统的不同，在 `pip install` 阶段，按照操作系统来编译
    - c 代码放在 `my_build/core`
2. 如何把 Python/C 编译为 `*.so`，然后被另一个 Python 项目打包。
    - 特点1：可以达到代码加密的效果，因为用户能接触到的是编译后的 `*.so` 文件
    - 特点2：编译过程是在打包时的机器上进行的，因此用户操作系统要一致才能运行
    - 代码放在 `core_private_source`，编译后，需要手动把 `*.so` 文件放在 `my_build/core_private` 
    - `setup.py` 中，把 `*.so` 文件以“数据文件”的形式加进去（`package_data`）
3. 把数据文件一起打包
    - 这样指定：`package_data={'my_build': ['data/*.txt', 'core_private/*.so']},`
4. 作为一个 Python 包打包发布 
 

如何运行？
```
pip install .
```

## 额外知识点 

多个 `*.c` 文件，且它们之间存在调用关系，如何办？
1. 按照 C 语言的规则整理各个文件，被调用的 `*.c` 文件，需要添加对应的 `*.h` 文件
2. 在 `setup.py` 中，把所有的  `*.c` 文件都列进去，但不要列 `*.h` 文件
 


更详细的文档 ：https://www.guofei.site/2021/09/12/hybrid.html
