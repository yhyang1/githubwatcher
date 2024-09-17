# GitHubWatcher

## 项目简介

**GitHubWatcher** 是一个用于监控 GitHub 项目动态的工具。它可以自动定期从 GitHub 获取项目数据，生成报告，发送通知，并允许用户订阅特定的 GitHub 项目。通过对 GitHub 项目数据（如 Stars、Forks、Issues 和 PRs）的监控，开发者和用户能够随时了解项目的成长和进展。

该项目使用 **Python** 编写，采用 **YAML** 文件管理配置，支持任务调度、报告生成、电子邮件通知和订阅管理功能。

## 功能

- **GitHub API 集成**: 从 GitHub 获取项目数据（Stars、Forks、Issues、Pull Requests 等）。
- **任务调度**: 使用 **APScheduler** 定时执行任务，自动获取项目数据。
- **数据通知**: 每次数据更新时发送通知邮件。
- **报告生成**: 自动生成 GitHub 项目的 PDF 报告，包括项目数据摘要。
- **订阅管理**: 允许用户订阅特定 GitHub 项目并定期接收更新报告。
- **配置管理**: 所有配置信息（如 GitHub API 访问、SMTP 服务器等）均通过 YAML 文件管理。

## 目录结构

```
GitHubWatcher/
├── src/                     # 源代码目录
│   ├── config.py            # 配置管理模块
│   ├── github_api.py        # GitHub API 集成
│   ├── scheduler.py         # 任务调度系统
│   ├── notification.py      # 邮件通知模块
│   ├── report_generator.py  # 报告生成模块
│   ├── subscription.py      # 订阅管理模块
├── tests/                   # 测试用例目录
│   ├── test_config.py       # 配置测试
│   ├── test_github_api.py   # GitHub API 测试
│   ├── test_scheduler.py    # 任务调度测试
│   ├── test_notification.py # 邮件通知测试
│   ├── test_report.py       # 报告生成测试
│   ├── test_subscription.py # 订阅管理测试
├── config.yaml              # 配置文件
├── requirements.txt         # Python 依赖包
├── README.md                # 项目说明文件
```

## 安装依赖

首先，确保你已经安装了 **Python 3.10** 或更高版本。

### 1. 创建虚拟环境并激活

```bash
python3 -m venv venv
source venv/bin/activate  # 对于 Windows 使用: venv\Scripts\activate
```

### 2. 安装项目依赖

```bash
pip install -r requirements.txt
```

依赖文件包含以下主要库：
- `requests`: 用于与 GitHub API 交互。
- `APScheduler`: 用于任务调度。
- `smtplib`: 用于发送电子邮件。
- `fpdf`: 用于生成 PDF 报告。
- `PyYAML`: 用于解析 YAML 配置文件。

## 配置项目

所有的配置信息都保存在 `config.yaml` 文件中。你需要根据你的具体情况修改此文件，特别是 GitHub API 令牌和 SMTP 邮件服务器信息。

### `config.yaml` 示例

```yaml
github:
  api_url: "https://api.github.com"
  access_token: "your_github_token"

smtp:
  server: "smtp.example.com"
  port: 587
  username: "yourusername"
  password: "yourpassword"
  from_email: "youremail@example.com"

scheduler:
  interval_hours: 1
```

- `github.api_url`: GitHub API 基本 URL（无需修改）。
- `github.access_token`: 你的 GitHub 访问令牌，用于访问 GitHub 数据。
- `smtp.server`, `smtp.port`, `smtp.username`, `smtp.password`, `smtp.from_email`: 这些配置用于发送通知邮件。
- `scheduler.interval_hours`: 任务调度的间隔时间（以小时为单位）。

## 运行项目

项目的主要功能模块如下：

### 1. GitHub 数据收集

通过 `github_api.py` 获取 GitHub 项目的基本信息：
```bash
python src/github_api.py
```

### 2. 启动任务调度

通过 `scheduler.py` 自动定时收集项目数据：
```bash
python src/scheduler.py
```

### 3. 发送电子邮件通知

配置 SMTP 邮件服务器后，通过 `notification.py` 发送电子邮件通知：
```bash
python src/notification.py
```

### 4. 生成项目报告

通过 `report_generator.py` 生成 GitHub 项目的 PDF 报告：
```bash
python src/report_generator.py
```

### 5. 订阅管理

通过 `subscription.py` 管理用户对 GitHub 项目的订阅：
```bash
python src/subscription.py
```

## 运行测试

本项目采用 **测试驱动开发** (TDD)，所有主要功能均有单元测试。要运行测试，使用以下命令：

```bash
python -m unittest discover tests/
```

此命令会运行 `tests/` 目录下的所有测试用例，确保项目的各个模块正常工作。

## 贡献指南

如果你想为 GitHubWatcher 做出贡献，请 fork 这个仓库并提交 pull request。我们欢迎任何形式的贡献，包括功能增强、Bug 修复和文档改进。

1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature-branch`)
3. 提交你的修改 (`git commit -m 'Add some feature'`)
4. 推送到分支 (`git push origin feature-branch`)
5. 提交一个 Pull Request

## 许可证

此项目采用 [MIT License](LICENSE) 许可证。详细信息请参阅 LICENSE 文件。
