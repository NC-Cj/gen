import subprocess

import argcomplete
import fire

MANAGERS = ["node", "git"]
REPOSITORIES = {
    "fastapi": {
        "normal": "",
        "easy": ""
    },
    "gin": {
        "normal": "",
        "easy": ""
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
    def fastapi(t: str):
        """
        fastapi web Project Scaffolding
        :param t:  Project type: Options[normal, normal-orm, easy]
        :return:
        """
        if t == 'clone':

        if t == 'clone':
            # 克隆项目
            try:
                result = subprocess.run(['git', 'clone', 'https://github.com/your-repo.git'], capture_output=True,
                                        text=True)
                if result.returncode == 0:
                    print("Project cloned successfully.")
                else:
                    print(f"\033[91mERROR:\033[0m Failed to clone project.")
                print(result.stdout)
                print(result.stderr)
            except subprocess.CalledProcessError as e:
                print(f"\033[91mERROR:\033[0m Failed to clone project: {e}")
        else:
            print(t)
        return

    @staticmethod
    def gin(t: str):
        """
        fastapi web Project Scaffolding
        :param t:  Project type: Options[normal, normal-orm, easy]
        :return:
        """
        pass


argcomplete.autocomplete(fire.Fire(Gen()))
