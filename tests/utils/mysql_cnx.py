from app.utils.models.database import Database


class DatabaseIntegrationBase:
    """Base Databasesetup for each database integrationtest."""

    def setup_class(self) -> None:
        """Will be executed once on Testclass initialization.

        Inits:
            self.db: Database Handler for class.
        """
        self.db = Database()
