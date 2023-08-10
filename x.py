import os
import shutil
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
        :type name: str
        :param t: Project type: Options[normal, normal-orm, easy]
        :type t: str
        :param orm: With PrismaORM management database
        :type orm: bool, default False

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

        url = REPOSITORIES["fastapi"]["repository"][t]

        try:
            result = subprocess.run(['git', 'clone', url], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"\033[91mERROR:\033[0m Failed to clone project.")

            # Get the cloned project directory name
            pwd = os.getcwd()
            directory_name = url.split('/')[-1].split('.')[0]
            project_dir = os.path.join(pwd, directory_name)
            git_dir = os.path.join(project_dir, '.git')

            if os.path.exists(git_dir):
                try:
                    shutil.rmtree(git_dir)
                except:
                    pass
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
