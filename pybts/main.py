import pybts
import argparse
import os


def directory_type(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid directory")
    return path


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="A simple program to demonstrate argparse")

    # 添加选项标志
    parser.add_argument("--dir", type=directory_type, help="Path to the log directory", required=True)
    # 添加debug参数
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    # 添加host参数
    parser.add_argument("--host", default="localhost", help="Host address")
    # 添加port参数
    parser.add_argument("--port", type=int, default=10000, help="Port number")

    # 添加-v, --version参数获取version
    parser.add_argument('-v', '--version', action='version', version=f'pybts {pybts.__version__}')

    # 解析命令行参数
    args = parser.parse_args()

    server = pybts.board_server.BoardServer(log_dir=args.dir, debug=args.debug, host=args.host, port=args.port)
    server.run()


if __name__ == '__main__':
    main()
