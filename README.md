# GTA5线上小助手内置Yimmenu附属资源

由于小助手已经停止更新，自动构建将仅用于Yimmenu的持续集成，小助手仅作为Yimmenu的临时注入器和Lua下载工具。小助手版Yimmenu已移除内部校验，dll不再与小助手绑定。

Kiddion等停止维护的工具将逐步移除以减小程序体积。

## 简介

此仓库存储GTA5线上小助手内置的Yimmenu的附属资源，包括Lua翻译文件、广告黑名单等，并进行持续集成。

YimV1 CI 源仓库: https://github.com/sch-lda/YimMenu/tree/upd-test \
YimV2直接使用官方仓库处理 \
自动构建从源仓库获取代码，经Crazyzhang开发的代码处理程序(闭源)处理后进行构建，生成的文件可以从Release或Artifacts获取，同时会在[Discord群组](https://crazyzhang.cn/discord/)推送构建完成通知。

自动构建依赖几个二进制文件，且存在鉴权，必须从外部以API的形式触发，且fork后无法运行。

小助手-exe https://github.com/sch-lda/yctest2/releases/download/CI/GTA5OnlineTools.exe \
小助手-源码 https://github.com/sch-lda/GTA5OnlineTools \
YimV1汉化版-dll https://github.com/sch-lda/yctest2/releases/download/CI/YimMenu.dll \
YimV1 sch分支-源码(与dll不完全相同,具体看该仓库Readme) https://github.com/sch-lda/YimMenu/tree/upd-test \
YimV2汉化版-dll https://github.com/sch-lda/yctest2/releases/download/CI/YimMenuV2.dll \
YimV2汉化版-源码(与构建dll所用源码完全一致) https://antfcc0.1007890.xyz/download_yimv2src \
以上链接对应的文件随自动构建工作流自动更新，链接通常不需要更改 

## 如何使用Issues和Pull request

 在此仓库中，您可以通过Pull request改进在线广告关键词黑名单(ad.json),或增加/改进Lua翻译(请查看Lua文件夹内的README.md)

 如果您的RID被错误的收录在ad_rid.json(小助手内置Yimmenu使用的在线广告机RID黑名单)中，请提交Issue，我会重新检查客户端自动提交的信息
 
## 文件结构:
```plaintext
Root
├── README.md
├── .github/workflows Yimmenu自动构建脚本 和 Lua翻译json合并脚本
├── CIprop 自动构建所需的二进制工具，包括代码处理程序下载、资源上传、推送通知到Discord等功能
├── Lua 储存一些英文Lua的语言文件，用于加载时翻译。详情请查看此文件夹内的README.md
├── ad.json 小助手内置Yimmenu使用的在线广告关键词黑名单
├── ad_rid.json 小助手内置Yimmenu使用的在线广告机RID黑名单(此文件由服务器上的程序自动生成，请勿提交Pr修改)
├── luatranslationmerger.py Lua翻译json合并脚本 调用的程序，由gpt生成
```

## 自动构建相关问题(复制自discord)

1.这些是什么？

自动化程序使用Yimmenu和小助手最新源代码自动构建的版本，没经过测试，可能不稳定，仅供有特殊需要的用户尝鲜使用。不代表小助手更新。小助手不可能跟随yim的更新频率，所以如果有体验最新yim需要的可以使用测试版小助手。

2.不同版本有什么区别？

我上传的一般包含yimmenu那边的未通过未广泛测试的代码，bugbot发布的是yimmenu那边已通过检查的，正式版小助手往往要再晚一些。

这三个版本相当于内测、公测、正式版。

我只在yimmenu那边有重大更新(涉及到游戏更新和反作弊修补)时发布内测，只有极少数人或者只有开发者自己测试过，具有较大的不确定性。文件或链接是以我的账号发布的。

<@1110145094574678017> 将在每次yimmenu官方正式合并更改时自动编译并更新固定链接指向的文件，同时使用bot的账号在这里推送更新通知。此版本与稳定版接近，正式版的yim通常也直接取自此版本，只是更新频率不同。

稳定版(正式版)仅由舰长亲自编译测试并推送到OTA通道 ，不跟随yim更新，更新周期可能在15-30天

3.如何使用测试版？

通过永久链接https://redirect.1007890.xyz/res1 下载测试版小助手，直接运行像往常一样操作。此链接始终指向最新文件，链接不需要变更，看到更新推送使用此链接重新下载即可。除非域名过期或出现其他故障

4.具体更新了什么，有意义吗？

不知道。也没有人专门去写更新日志。有能力的可以去Yimmenu官方GitHub查提交记录。即使是一个小字符串的修改甚至是问题反馈模板的修改也会触发一次自动构建,中文翻译的变更也会触发构建，用户可能无法在实际体验中感受到区别。所以测试版不一定能解决你当前遇到的问题。

5.发现问题怎样反馈？

若测试版出现构建失败、汉化不全(YimMenu界面存在英文大写乱码)，无需反馈，一般会在正式版修复。

若测试版Yimmenu出现功能异常，而正式版正常，请反馈以避免此问题进入正式版。反馈时注明是测试版的问题。

6.为什么更新那么频繁？

yimmenu、小助手、yimmenu汉化程序 任何一个有代码提交就会触发一次自动构建。重要信息不会在这里发布，建议将本频道静音，切勿反馈通知打扰问题。Discord支持将特定频道完全静音，静音后不会收到推送通知，也不会有圆点。

7.测试版支持应用内更新吗？

不支持，你只能通过这里提供的链接下载最新测试版。测试版的应用内更新只能更新到下一个正式版。此外测试版不会有额外的版本号，版本号与正式版相同，你需要在这里发布新的测试版通知时手动重新下载并删掉旧的exe
