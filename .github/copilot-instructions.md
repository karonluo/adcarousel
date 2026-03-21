# ADCarousel - GitHub Copilot 使用说明

## 项目简介

ADCarousel 是一个基于 Django 的简易广告轮播工具，支持上传背景图片、配置文字颜色/大小/位置以及时间显示格式。

## 技术栈

- **语言**: Python 3.10
- **框架**: Django 5.1
- **数据库**: MySQL 8.0
- **前端**: Bootstrap 4.5, jQuery 3.6

## 项目结构

```
adcarousel/         # Django 项目配置目录
  settings.py       # 项目设置（数据库、语言、静态文件等）
  urls.py           # 项目路由配置
app/                # 主应用目录
  models.py         # 数据模型
  views.py          # 视图逻辑
  static/templates/ # HTML 模板
manage.py           # Django 管理命令入口
requirements.txt    # Python 依赖（UTF-8 编码）
InitDB.sql          # 数据库初始化脚本
```

## 开发环境配置

1. 安装 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 初始化数据库（MySQL 8.0），执行 `InitDB.sql`
3. 运行开发服务器：
   ```bash
   python manage.py runserver
   ```
