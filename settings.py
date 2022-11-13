
class settings:
    def __init__(self, database_connection, auto_close_seconds = 60):
        self.database_connection = database_connection
        self.auto_close_feature_on = True
        self.auto_close_seconds = auto_close_seconds

    def get_auto_close_setting(self):
        try:
            auto_close_setting_on = self.database_connection.get_data("SELECT AutoClose FROM Settings ORDER BY SettingsId DESC LIMIT 1")
            self.auto_close_feature_on = auto_close_setting_on
        finally:
            return self.auto_close_feature_on

    def get_auto_close_seconds_setting(self):
        try:
            auto_close_setting_seconds = self.database_connection.get_data("SELECT CloseAfter FROM Settings ORDER BY SettingsId DESC LIMIT 1")
            self.auto_close_seconds = auto_close_setting_seconds
        finally:
            return self.auto_close_seconds

