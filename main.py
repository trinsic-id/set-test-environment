import argparse
import logging
from ast import literal_eval
from typing import Tuple


def get_known_environment(env_name: str) -> Tuple[str, str, str]:
    known_environments = {
        "dev": ("dev-internal.trinsic.cloud", "443", "true"),
        "staging": ("staging-internal.trinsic.cloud", "443", "true"),
        "prod": ("prod.trinsic.cloud", "443", "true"),
    }
    return known_environments[env_name]



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "serverEndpoint", help="Server endpoint options: string, array of strings"
    )
    parser.add_argument(
        "serverPort", help="Server port options: string, array of strings"
    )
    parser.add_argument("useTls", help="Server tls options: string, array of strings")
    parser.add_argument(
        "knownEnvironment",
        help="Server environment",
        choices=["dev", "staging", "prod"],
        default=""
    )

    args = parser.parse_args()
    logging.info(f"Parsed args={args}")

    server_endpoint = eval_input(args.serverEndpoint)
    server_port = eval_input(args.serverPort)
    server_use_tls = eval_input(args.useTls)

    if args.knownEnvironment:
        server_endpoint, server_port, server_use_tls = get_known_environment(args.knownEnvironment)

    # Print the desired output
    print(f"::set-output name=serverEndpoint::{server_endpoint}")
    print(f"::set-output name=serverPort::{server_port}")
    print(f"::set-output name=useTls::{server_use_tls}")


def eval_input(input_str: str) -> str:
    # Evaluates string to see if it is a valid python literal, no code execution.
    input_value = literal_eval(input_str)
    # If string, take it, if list, pick first non-empty
    if isinstance(input_value, list):
        input_value = [x for x in input_value if x][0]
    if isinstance(input_value, int):
        input_value = str(input_value)
    return input_value


if __name__ == "__main__":
    main()
