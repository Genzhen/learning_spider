#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hello.py
@Time    :   2020-11-06
@Author  :   EvilRecluse
@Contact :   https://github.com/RecluseXU
@Desc    :   
    asyncio 是用来编写 并发 代码的库，使用 async/await 语法。
    asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。
    asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。
'''

# here put the import lib
import asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())