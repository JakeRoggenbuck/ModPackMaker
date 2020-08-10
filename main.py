from os import listdir
from os.path import isfile, join
import regex as re
import inquirer
import subprocess


class Mods:
    def __init__(self):
        self.path = "./mods/"
        self.version = self.get_version()
        self.mods = self.get_files(self.path)
        self.version_mods = self.get_versioned_files(self.version, self.mods)
        self.picked_mods = self.get_mods(self.version_mods)
        self.command = self.zip_command(self.picked_mods)

    def get_files(self, mypath):
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        return onlyfiles

    def get_versioned_files(self, version, files):
        version_mods = [mod for mod in files if re.search(version, mod)]
        return version_mods

    def get_mods(self, mods):
        questions = [inquirer.Checkbox("mods", message="Mods", choices=mods)]
        answers = inquirer.prompt(questions)
        return answers

    def get_version(self):
        version = input("What version: ")
        return version

    def zip_command(self, mod_list):
        command = "zip mods "
        for mod in mod_list["mods"]:
            command += "mods/" + mod + " "
        return command

    def run_command(self, command):
        print("saving as mod.zip")
        subprocess.run([command], shell=True)

if __name__ == "__main__":
    mod = Mods()
    mod.run_command(mod.command)
