# Lua中文语言文件仓库

此翻译方式为劫持翻译，将Lua传入Yimmenu的显示相关API的参数进行实时替换。这个文件夹存储英文到中文的字符串对应关系。

luas文件夹存放各英文lua的语言文件，格式为json，文件名应为英文lua文件名，如`DailyCollectibles.json`。

lua_lang.json由Github Action自动生成，合并luas文件夹的所有json，无需手动修改。客户端将获取此文件进行翻译。