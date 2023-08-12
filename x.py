import contextlib
import json
import os
import shutil
import subprocess

import argcomplete
import fire


def _check_command_exists(command):
    try:
        subprocess.check_output([command, '--version'])
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        print(f"\033[91mERROR:\033[0m Your system needs to have {command}")


def _clone(url):
    result = subprocess.run(['git', 'clone', url], capture_output=True, text=True)
    if result.returncode != 0:
        print("\033[91mERROR:\033[0m Failed to clone project.")

    pwd = os.getcwd()
    directory_name = url.split('/')[-1].split('.')[0]
    project_dir = os.path.join(pwd, directory_name)
    git_dir = os.path.join(project_dir, '.git')

    return pwd, project_dir, git_dir


def _delete_git_directory(git_dir):
    if os.path.exists(git_dir):
        with contextlib.suppress(Exception):
            shutil.rmtree(git_dir)


def _rename(project_dir, pwd, name):
    # os.rename(project_dir, os.path.join(pwd, name))
    # os.rename("./gen-fastapi-norm", f"./{name}")
    shutil.move(project_dir, os.path.join(pwd, name))


class Gen(object):

    def __init__(self):
        with open("config.json", 'r') as file:
            self.config = json.load(file)

        for value in self.config["managers"]:
            _check_command_exists(value)

    def fastapi(self, name: str, t: str, orm: bool = False):
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
                self.config["commands"]["checkPrisma"],
                shell=True,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            if "prisma" not in output:
                print("\033[93mWARNING:\033[0m Prisma package is not installed, enter `npm install -g prisma`.")
                return

        url = self.config["repositories"]["fastapi"]["repository"][t]
        pwd, project_dir, git_dir = _clone(url)

        _delete_git_directory(git_dir)
        _rename(project_dir, pwd, name)

        # print(f"\033[91mERROR:\033[0m Failed to clone project: {e}")

    def gin(self, t: str):
        """
        fastapi web Project Scaffolding
        :param t:  Project type: Options[normal, normal-orm, easy]
        :return:
        """
        pass


argcomplete.autocomplete(fire.Fire(Gen()))
