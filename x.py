import os
import subprocess

import argcomplete
import fire

MANAGERS = ["node", "git"]
REPOSITORIES = {
    "fastapi": {
        "repository": {
            "normal": "git@github.com:NC-Cj/gen-fastapi-norm.git",
            "easy": ""
        },
        "name": "gen-fastapi-norm"
    },
    "gin": {
        "repository": {
            "normal": "git@github.com:NC-Cj/gen-fastapi-norm.git",
            "easy": ""
        },
        "name": "gen-fastapi-norm"
    }
}
COMMANDS = {
    "checkPrisma": "npm -g list --depth=0 prisma",
    "clone": "git clone --bare",
}


def check_command_exists(command):
    try:
        subprocess.check_output([command, '--version'])
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        print(f"\033[91mERROR:\033[0m Your system needs to have {command}")


class Gen(object):

    def __init__(self):
        for value in MANAGERS:
            check_command_exists(value)

    @staticmethod
    def fastapi(name: str, t: str, orm: bool = False):
        """
        fastapi web Project Scaffolding

        :param name:You project Name
        :param t: Project type: Options[normal, normal-orm, easy]
        :param orm:Bool, default False, With PrismaORM management database

        :Example:

        The following examples show how to use the `fastapi` command:

        1. Standard FastAPI web engineering directory:
           ```
           gen fastapi -t normal
           ```

        2. Standard FastAPI web engineering directory with PrismaORM management database:
           ```
           gen fastapi -t normal-orm
           ```

        3. The most concise project:
           ```
           gen fastapi -t easy
           ```
        """

        if orm:
            output = subprocess.check_output(
                COMMANDS["checkPrisma"],
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            if "prisma" not in output:
                print("\033[93mWARNING:\033[0m Prisma package is not installed, enter `npm install -g prisma`.")
                return

        url = REPOSITORIES["fastapi"]["repository"][t]

        try:
            result = subprocess.run(['git', 'clone', url], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"\033[91mERROR:\033[0m Failed to clone project.")

            pwd = os.getcwd()
            directory_name = url.split('/')[-1].split('.')[0]
            project_dir = os.path.join(pwd, directory_name)
            git_dir = os.path.join(project_dir, '.git')

            if os.path.exists(git_dir):
                os.rename(project_dir, os.path.join(pwd, name))

        except subprocess.CalledProcessError as e:
            print(f"\033[91mERROR:\033[0m Failed to clone project: {e}")

    @staticmethod
    def gin(t: str):
        """
        fastapi web Project Scaffolding
        :param t:  Project type: Options[normal, normal-orm, easy]
        :return:
        """
        pass


argcomplete.autocomplete(fire.Fire(Gen()))
