from .monitor import Monitor  # 使用相对导入
import sys
import time

def main():
    if len(sys.argv) != 4:
        print("用法: python -m src.main <网址> <监测间隔（秒）> <触发告警关键词>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        interval = int(sys.argv[2])
    except ValueError:
        print("监测间隔必须是整数秒")
        sys.exit(1)
    keyword = sys.argv[3]

    print(f"开始监控: URL={url}, 间隔={interval}秒, 关键词='{keyword}'")
    
    monitor = Monitor(url, interval, keyword)
    monitor.start()
    
    print("监控已启动，按Ctrl+C停止...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("正在停止监控...")
        monitor.pause()
        print("监控已停止")
    except Exception as e:
        print(f"发生未预期的错误: {e}")
    finally:
        if monitor and monitor.driver:
            monitor.driver.quit()

if __name__ == "__main__":
    main()