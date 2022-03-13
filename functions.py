"""Functions."""
from libqtile.command import lazy
# from libqtile.command_client import InteractiveCommandClient


class Functions:
    """Function class."""

    @staticmethod
    def window_to_prev_group():
        """Window to previous group."""
        @lazy.function
        def __inner(qtile):
            i = qtile.groups.index(qtile.current_group)

            if qtile.current_window and i != 0:
                group = qtile.groups[i - 1].name
                qtile.current_window.togroup(group, switch_group=True)

        return __inner

    @staticmethod
    def window_to_next_group():
        """Window to next group."""
        @lazy.function
        def __inner(qtile):
            i = qtile.groups.index(qtile.current_group)

            if qtile.current_window and i != len(qtile.groups):
                group = qtile.groups[i + 1].name
                qtile.current_window.togroup(group, switch_group=True)

        return __inner

    @staticmethod
    def kill_all_windows():
        """Kill all windows."""
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                window.kill()

        return __inner

    @staticmethod
    def kill_all_windows_minus_current():
        """Kill all windows except current one."""
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                if window != qtile.current_window:
                    window.kill()

        return __inner


class PWA:
    """PWA class."""

    def __init__(self):
        """Init."""
        pass

    @staticmethod
    def notion():
        """Notion."""
        return "brave --profile-directory=Default --app=https://notion.so"

    @staticmethod
    def music():
        """Music."""
        return "brave --profile-directory=Default \
--app=https://music.youtube.com/"

    @staticmethod
    def spotify():
        """Spotify."""
        return "brave --profile-directory=Default \
--app=https://open.spotify.com/"

    @staticmethod
    def youtube():
        """Youtube."""
        return "brave --user-data-dir=Default --app=https://www.youtube.com"

    @staticmethod
    def calendar():
        """Calendar."""
        return "brave --profile-directory=Default \
--app=https://calendar.google.com/calendar/"

    @staticmethod
    def habitica():
        """Habitica."""
        return "brave --profile-directory=Default --app=https://habitica.com/"


if __name__ == "__main__":
    print("This is an utilities module")
