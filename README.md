# TexToPdf

## 目录

- [项目介绍](#项目介绍)
- [功能特性](#功能特性)
- [项目结构](#项目结构)
- [安装方法](#安装方法)
- [使用方法](#使用方法)
- [项目进度追踪](#项目进度追踪)
  - [功能开发](#功能开发)
  - [文档和示例](#文档和示例)
  - [测试和验证](#测试和验证)

## 项目介绍

TexToPdf 是一个基于 Python 开发的后端，专门用于处理 TeX 代码到 PDF 的实时编译。该服务提供 RESTful API 接口，与前端应用（tex_to_pdf_vue3）配合使用，实现完整的在线 TeX 编辑器功能，包括实时预览和 PDF 下载。

## 功能特性

- TeX 代码编译
- PDF 生成
- RESTful API 接口
- 基本错误检测
- PDF 文件下载

## 项目结构

```
TexToPdf/
├── app.py                   # 应用入口
├── config.py                # 配置文件
├── requirements.txt         # 依赖包列表
├── utils/                   # 工具函数目录
│   ├── __init__.py          # 初始化文件
│   └── tex_converter.py     # TeX 转换工具
├── api/                     # API 目录
│   ├── __init__.py          # 初始化文件
│   ├── routes.py            # 路由定义
│   └── models.py            # 数据模型
├── services/                # 服务层
│   ├── __init__.py          # 初始化文件
│   └── compilation.py       # 编译服务
├── tests/                   # 测试目录
│   ├── __init__.py          # 初始化文件
│   ├── test_api.py          # API 测试
│   └── test_compiler.py     # 编译器测试
├── static/                  # 静态文件目录
│   └── temp/                # 临时文件存储
├── .env.example             # 环境变量示例
└── README.md                # 项目说明
```

## 安装方法

- 克隆仓库

```bash
git clone https://github.com/AlcMaple/TexToPdf.git
cd TexToPdf
```

- 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

- 启动服务器

```bash
python app.py
```

## 🚀 项目进度追踪

### 📋 功能开发
| 状态 | 功能 | 备注 |
|:---:|---|---|
| ✅ | 项目基础结构 | 基本文件结构和模块划分 |
| ⬜ | TeX 编译核心功能 | 使用 pdflatex 编译 TeX 代码 |
| ⬜ | API 路由设置 | RESTful API 接口实现 |
| ⬜ | 错误处理机制 | 捕获和格式化编译错误 |
| ⬜ | PDF 生成和管理 | 生成、存储和提供 PDF 下载 |
| ⬜ | 性能优化 | 加快编译速度 |
| ⬜ | 临时文件管理 | 自动清理和维护临时文件 |

### 📋 文档和示例
| 状态 | 任务 | 备注 |
|:---:|---|---|
| ✅ | README.md | 基本项目介绍和进度跟踪 |
| ⬜ | 安装指南 | 各系统详细安装指南 |

### 📋 测试和验证
| 状态 | 任务 | 备注 |
|:---:|---|---|
| ⬜ | 单元测试 | 核心函数测试 |
| ⬜ | API 测试 | 接口功能测试 |
| ⬜ | 集成测试 | 与前端集成测试 |