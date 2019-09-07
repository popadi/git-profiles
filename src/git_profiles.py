from src.executor import executor, parser

if __name__ == "__main__":
    parser = parser.get_arguments_parser()
    arguments = parser.parse_args()
    executor.execute_command(arguments)
