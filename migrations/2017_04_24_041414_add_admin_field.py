from orator.migrations import Migration


class AddAdminField(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.boolean("admin").default(False)

    def down(self):
        """
        Revert the migrations.
        """
        pass
