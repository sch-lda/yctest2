# Lua中文语言文件仓库

此翻译方式为劫持翻译，将Lua传入Yimmenu的显示相关API的参数进行实时替换。这个文件夹存储英文到中文的字符串对应关系。

luas文件夹存放各英文lua的语言文件，格式为json，文件名应为英文lua文件名，如`DailyCollectibles.json`。

lua_lang.json由Github Action自动生成，合并luas文件夹的所有json，无需手动修改。客户端将获取此文件进行翻译。

Json中`"Teleport to Vehicle": "传送到载具",`左侧的成为键(Key),右侧的成为值(Value).键(Key)为英文Lua中原始的字符串,值(Value)为对应的中文翻译.

键(Key)中不能出现转义字符，例如`\n`.译者应在json文件里将`\n`写为`\\n`避免json文件在合并时出错,用户使用时Yimmenu将自动完成识别.

正确示例:
```json
    " is available.\\nWarning: Tunable is not active.": " 可用.\n警告: 可调整项未激活.",
```
错误示例1:
```json
    " is available.\nWarning: Tunable is not active.": " 可用.\n警告: 可调整项未激活.",
```
错误示例2:
```json
    " is available.\nWarning: Tunable is not active.": " 可用.\\n警告: 可调整项未激活.",
```
错误示例3:
```json
    " is available.\\nWarning: Tunable is not active.": " 可用.\\n警告: 可调整项未激活.",
```

注: 如果遇到lua作者使用`\10`代替`\n`的情况，翻译时键和值都按`\n`处理，因为Yimmenu会自动将`\10`转换为`\n`。

## 已翻译Lua

- [DailyCollectibles](https://github.com/YimMenu-Lua/DailyCollectibles)

- [RandomEvents](https://github.com/YimMenu-Lua/RandomEvents)

- [MiniGameHack](https://github.com/YimMenu-Lua/MiniGameHack)

- [GanVan](https://github.com/YimMenu-Lua/GunVan)

- [TokyoDrift](https://github.com/YimMenu-Lua/TokyoDrift)

- [YimResupplier](https://github.com/YimMenu-Lua/YimResupplier)

- [Extras-Addon-for-YimMenu](https://github.com/Deadlineem/Extras-Addon-for-YimMenu)

- [PayphoneHits](https://github.com/YimMenu-Lua/PayphoneHits)

- [YimMenu-HeistLua](https://github.com/wangzixuank/YimMenu-HeistLua)

## 使用方法

方法1: 下载[小助手测试版](https://github.com/sch-lda/yctest2/releases/tag/CI), 导入受支持的Lua, 将自动进行翻译

方法2: 从源代码构建 https://github.com/sch-lda/YimMenu/tree/upd-test