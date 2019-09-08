from src.executor import executor, parser


def main():
    p = parser.get_arguments_parser()
    arguments = p.parse_args()
    executor.execute_command(arguments)


if __name__ == "__main__":
    main()
