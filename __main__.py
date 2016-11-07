import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_helpers

dev_helpers.attach_to_cloudshell()

from sandbox_scripts.environment.setup.setup_script import EnvironmentSetup


def main():
    EnvironmentSetup().execute()


if __name__ == "__main__":
    main()
