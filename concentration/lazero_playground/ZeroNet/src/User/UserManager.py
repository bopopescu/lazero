# Included modules
import json
import logging
import time

# ZeroNet Modules
from .User import User
from Plugin import PluginManager
from Config import config


@PluginManager.acceptPlugins
class UserManager(object):
    def __init__(self):
        self.users = {}
        self.log = logging.getLogger("UserManager")

    # Load all user from data/users.json
    def load(self):
        if not self.users:
            self.users = {}

        user_found = []
        added = 0
        s = time.time()
        # Load new users
        try:
            json_path = "%s/users.json" % config.data_dir
            data = json.load(open(json_path))
        except Exception as err:
            raise Exception("Unable to load %s: %s" % (json_path, err))

        for main_address, data in list(data.items()):
            if main_address not in self.users:
                user = User(main_address, data=data)
                self.users[main_address] = user
                added += 1
            user_found.append(main_address)

        # Remove deleted adresses
        for main_address in list(self.users.keys()):
            if main_address not in user_found:
                del(self.users[main_address])
                self.log.debug("Removed user: %s" % main_address)

        if added:
            self.log.debug("Added %s users in %.3fs" % (added, time.time() - s))

    # Create new user
    # Return: User
    def create(self, main_address=None, main_seed=None):
        self.list()  # Load the users if it's not loaded yet
        user = User(main_address, main_seed)
        self.log.debug("Created user: %s" % user.main_address)
        if user.main_address:  # If successfully created
            self.users[user.main_address] = user
            user.saveDelayed()
        return user

    # List all users from data/users.json
    # Return: {"usermainaddr": User}
    def list(self):
        if self.users == {}:  # Not loaded yet
            self.load()
        return self.users

    # Get user based on main_address
    # Return: User or None
    def get(self, main_address=None):
        users = self.list()
        if users:
            return list(users.values())[0]  # Single user mode, always return the first
        else:
            return None


user_manager = UserManager()  # Singleton
