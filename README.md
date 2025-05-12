# DateServer MCP 服务

本项目为基于 FastMCP 的本地日期与时间工具服务，支持 MCP 协议，可在本地运行并通过 Cherry Studio 等 MCP 客户端调用。

---

## 部署与使用说明

### 1. 环境准备
- 推荐 Python 3.8 及以上版本
- 建议使用虚拟环境隔离依赖

### 2. 克隆代码
```bash
git clone https://github.com/panpeter2024/date_mcp
cd date_mcp
```

### 3. 创建虚拟环境并安装依赖
#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install fastmcp
```
#### Windows
```bat
python -m venv venv
venv\Scripts\activate
pip install fastmcp
```

### 4. 启动服务
- **macOS/Linux**:
  ```bash
  nohup venv/bin/python server_date.py > mcp.log 2>&1 &
  ```
- **Windows**:
  ```bat
  python server_date.py
  ```

### 5. 在 Cherry Studio 配置 MCP 服务
- 服务名称：本地日期服务
- MCP服务地址：`http://127.0.0.1:9000/sse`
- 传输方式：SSE
- 认证/Key：留空

### 6. 常用命令
- 查看日志：
  - **macOS/Linux**:
    ```bash
    tail -f mcp.log
    ```
  - **Windows**:
    ```bat
    type mcp.log
    ```
- 停止服务：
  - **macOS/Linux**:
    ```bash
    ps aux | grep server_date.py
    kill <进程号>
    ```
  - **Windows**:
    在任务管理器中结束 `python.exe` 进程，或关闭命令行窗口。

---

## 工具列表
- get_current_date：获取当前日期（YYYY-MM-DD）
- get_current_time：获取当前时间（HH:MM:SS）
- get_current_weekday：获取今天是星期几（中文）
- get_current_timestamp：获取当前Unix时间戳（秒）
- get_current_iso_datetime：获取当前日期和时间（ISO 8601 格式）

---

## 说明
- 本服务仅在本地运行，无需公网暴露。
- 如需自定义端口或扩展功能，请修改 `server_date.py`。
