from orator.migrations import Migration


class RenameUserIdPk(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.rename_column("id", "pk")

    def down(self):
        """
        Revert the migrations.
        """
        pass
