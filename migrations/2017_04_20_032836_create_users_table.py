from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.big_increments('id')
            table.timestamps()
            table.soft_deletes()

            table.string("name")
            table.string("username").unique()
            table.string("email").unique()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
