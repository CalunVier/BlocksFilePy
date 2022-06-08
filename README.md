# BlocksFilePy
基于python的简易python分块加密存储程序


## 系统的文件构成与定义

```
FSRootDir
	|-mft
    |-temp/
        |-tempfiles...
	|-blocks/
		|-00
			|-...
		|-01
		.....
```
其中所有数据都应当是加密后的数据，即用户应当在访问前知晓其加解密方式及密码。
<!-- ### mft.dat 定义

#### 文件表定义

| 偏移量                   |位数| 定义                                    |
| -------------------------| | --------------------------------------- |
| [0,32]                 | 32 | 头偏移量(0为没有头)                     |
| [65, head_end]           | head_length | 头元数据                                |
| [head_end+1, head_end+32]| 32 | 文件表内容大小（文件表不会超过4GB吧？） |
| ...                      | | ...                                     |

#### 元数据块定义

| 偏移量          | 位数         | 定义                |
| --------------- | ------------ | ------------------- |
| [0, 32]         | 32           | keyname(ASCII only) |
| [33, 64]        | 32           | value长度           |
| [65, value_end] | value_length | value               |

#### 文件表头定义

| Key            | 位数 | Value |
| -------------- | ---- | ----- |
| HASH_METHOD    | 8    | 00-FF |
| BLOCK_LENGHT   | 8    | 00-FF |
| ENCRYPT_METHOD | 8    | 00-FF |

#### 哈希方法定义

| 哈希方法 | 值(HEX) |
| -------- | ------- |
| SHA-256  | 00      |
| SHA-512  | 01      |
| MD5      | 02      |
| SHA-1    | 03      |

#### 加密方法定义

| 加密方法 | 值(HEX) |
| -------- | ------- |
| AES-XTS  | 00      |
| AES-CBC  | 01      |
| AES-GCM  | 02      |
| RSA2048  | 03      |
| RSA3072  | 04      |
| RSA4096  | 05      |
| RSA8192  | 06      |

#### 文件表内容定义

| 偏移量|位数| 定义                       |
| -------- |--| -------------------------- |
| 0        | 4 |文件类型（0文件，1文件夹） |
| [5,64]  | 60 |文件ID                     |
| [65, 96] | 32 | 文件名长度(name) |
| [97, name_end] | name_length | 文件名 |
|  | 64 | 文件大小 |
| [name_end+1, name_end+32] | 32                | 存储块信息长度(blocks_inf) |
| [name_end+65, blocks_inf_end] | blocks_inf_length | 文件块信息 |
| [blocks_inf_end+1， hash_end] | hash_end | 文件哈希 |
|  | 32 | 元数据偏移量 |
|  | meta_length | 元数据块 |

#### 文件块信息定义

| 偏移量                     | 位数         | 定义   |
| -------------------------- | ------------ | ------ |
| [0, BLOCK_LENGHT]          | BLOCK_LENGHT | 块ID   |
| [BLOCK_LENGHT+1, HASH_END] | HASH_LENGTH  | 块哈希 |
|                            | 64           | 块大小 | -->

### 基于JSON的MFT文件
基本格式

```javascript
{
    "HEAD":{
        "HASH-METHOD": 0,
        "ENCRYPT_METHOD": 0,
        "MAX_BLOCK_SIZE": 10240, // 单位：字节。10240是10KB
        "LEVEL_SIZE": 8,    // 文件系统中每级指针的长度，对于8，则有2个16进制位标识，其应当是4的倍数。
        "POINT_SIZE": 16,   // 块指针长度，应当是LEVEL_SIZE的倍数[8, 16, 32, 64]
        "PUBLICK_KEY":""	// 如果需要
	},
	"BODY":[
        [
            0,		// 文件类型
            123, 	// 文件ID
            "文件名",
            123, 	// 文件大小
            "hash",
            [ //块列表
                ["ABCDEF", 123/*块大小*/,"hash"]
            ],
            {/*元数据*/}
        ]
    ]
}
```
### 基于JSON的config文件
基本格式

```javascript
{
    "OPTION_KEY": "VALUE"
    // etc.
}
```

### 支持的加密方法

| 加密方法 | 字符串值 | 数值(HEX) |
| -------- | -------- | ------- |
| AES-XTS  | AES-XTS  | 00      |
| AES-CBC  | AES-CBC  | 01      |
| AES-GCM  | AES-GCM  | 02      |
<!-- | RSA2048  | RSA2048  | 03      |
| RSA3072  | RSA3072  | 04      |
| RSA4096  | RSA4096  | 05      |
| RSA8192  | RSA8192  | 06      | -->

其中字符串值不区分大小写

### 支持的哈希方法

| 哈希方法 | 字符串值 | 数值(HEX) |
| -------- | ------- | ------- |
| SHA-256  | SHA-256  | 00      |
| SHA-512  | SHA-512  | 01      |
| MD5      |    MD5   | 02      |
| SHA-1    | SHA-1    | 03      |

### 块文件目录
我们使用16进制的文件名标记块指针。例如级长度为8位的系统，32位长度块"B25F132A"，其对应的块应当保存在目录/root/B2/5F/13/2A。我们使用这样的目录结构以优化不同文件系统下的索引性能。

## 用户功能
本节展示我们的设计思路、目标和计划，其中包含已经完成的未完成的部分。主要聚焦于用户视角。

### 命令行
<!-- ```bash
    -a --add
``` -->
- init \<soucre\> 在指定目录（如果不存在则创建）创建BFS
    - \-\-method "\<method\>"加密方法
    - \-\-mft \<source\>文件表
    - \-p \-\-password "\<password\>"密码
    - \-\-blocksdir \<source\>  块文件夹
    - \-\-hash "\<value\>"  哈希方法
    - \-\-config \<source\> 载入config文件
- open \<source\> 打开目录（打开BFS）
    - \-\-method "\<method\>"   加密方法
    - \-\-mft \<source\>文件表
    - \-p \-\-password "\<password\>"密码
    - \-\-workpath \<source\>工作目录
    - \-\-blocksdir \<source\>  块文件夹
    - \-\-config \<source\> 载入config文件
- add \<out_path\> \<interal_path\> 添加文件到缓存（计划）
    - \-r   递归加入
- reset 撤销添加
    - \-r 递归撤销
- rm \<internal_path\> 删除一个文件
    - \-r 递归删除
- commit 提交更改，输出变更文件以及变更日志
- status 查看当前缓存
- check \<internal_path\> 检查指定文件（列出所对应的块）
- export \<internal_path\>
    - \-o 指定输出位置（默认输出到 标准输出）
    - \-s \-\-source 指定源（默认从blocks文件夹中直接获取）
- ls \<internal_path\> 打印指定目录的文件列表
    - \-o \-\-out 打印外部目录
- cd \<internal_dir\> 进入目录
    - \-o 变更外部工作目录
- config \<option\> \<value\> 变更设置
- help 帮助

### config包含
```javascript
{
    "method": "method", // 存放块文件的目录
    "mft": "",
    "blocksdir": "",
    "hash": ""
}
```



