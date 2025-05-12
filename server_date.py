from fastmcp import FastMCP
from datetime import date, datetime
import time

# 创建MCP服务，命名为DateServer
mcp = FastMCP("DateServer", port=9000)

@mcp.tool()
def get_current_date() -> str:
    """获取当前日期，格式为YYYY-MM-DD"""
    return date.today().isoformat()

@mcp.tool()
def get_current_time() -> str:
    """获取当前时间，格式为HH:MM:SS"""
    return datetime.now().strftime("%H:%M:%S")

@mcp.tool()
def get_current_weekday() -> str:
    """获取今天是星期几（中文）"""
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return weekdays[date.today().weekday()]

@mcp.tool()
def get_current_timestamp() -> int:
    """获取当前Unix时间戳（秒）"""
    return int(time.time())

@mcp.tool()
def get_current_iso_datetime() -> str:
    """获取当前日期和时间，ISO 8601格式"""
    return datetime.now().isoformat()

if __name__ == "__main__":
    # 支持SSE方式运行
    mcp.run(transport="sse") 